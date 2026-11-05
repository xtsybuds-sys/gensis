"""The primordial soup pilot: cells compete for nutrients, mutate, and reproduce.

Design approved by Muse (2026-11-05), nutrient-only. The pilot answers one question:
does measurable complexity grow from mutation plus selection on a simple substrate?
If it does not, the cells-to-humans path is not worth pursuing and is reported as a
negative result, not tuned until it passes.
"""

from __future__ import annotations

import math
import random
import time
from collections import defaultdict

from ..util import TAU, clamp, mean, stable_hash
from .dish import NutrientDish
from .genome import GENE_NAMES, Genome

TARGET_GENERATIONS = 20000
SUCCESS_MEDIAN_DEPTH = 100
SUCCESS_NICHE_GROWTH = 2.0
SUCCESS_TRAIT_Z = 2.0
SURVIVAL_FLOOR_GEN = 10000

_UPTAKE = 0.12
_BASE_COST = 0.006
_MOVE_COST = 0.35
_CROWD_COST = 0.002
_TURN_RATE = 1.5
_CHILD_OFFSET = 0.05


def _wrap(angle):
    while angle > math.pi:
        angle -= TAU
    while angle < -math.pi:
        angle += TAU
    return angle


class Cell:
    __slots__ = ("x", "y", "heading", "energy", "age", "genome", "gen", "lineage", "alive")

    def __init__(self, x, y, heading, energy, genome, gen, lineage):
        self.x = x
        self.y = y
        self.heading = heading
        self.energy = energy
        self.age = 0
        self.genome = genome
        self.gen = gen
        self.lineage = lineage
        self.alive = True


def _crowding(cells, buckets):
    buckets.clear()
    for cell in cells:
        key = (int(cell.x * 2.0), int(cell.y * 2.0))
        buckets[key] = buckets.get(key, 0) + 1
    return buckets


def _neighbours(cell, buckets):
    cx = int(cell.x * 2.0)
    cy = int(cell.y * 2.0)
    total = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            total += buckets.get((cx + dx, cy + dy), 0)
    return total - 1


def _snapshot(cells, lineages, ticks):
    if not cells:
        return {
            "population": 0,
            "median_depth": 0,
            "max_depth": 0,
            "diversity": 0.0,
            "niche_breadth": 0.0,
            "traits": {},
            "ticks": ticks,
        }
    sample = cells[:150]
    pairs = 0
    total = 0.0
    for i in range(len(sample)):
        for j in range(i + 1, len(sample)):
            total += sample[i].genome.distance(sample[j].genome)
            pairs += 1
    depths = sorted(cell.gen for cell in cells)
    niches = sorted(len(lineages[cell.lineage]) for cell in cells)
    traits = {
        name: round(mean(cell.genome.values[i] for cell in cells), 6)
        for i, name in enumerate(GENE_NAMES)
    }
    return {
        "population": len(cells),
        "median_depth": depths[len(depths) // 2],
        "max_depth": depths[-1],
        "diversity": round(total / pairs, 6) if pairs else 0.0,
        "niche_breadth": float(niches[len(niches) // 2]),
        "traits": traits,
        "ticks": ticks,
    }


def run_pilot(seed, generations=TARGET_GENERATIONS, minutes=45.0, initial=200,
              cap=600, size_m=16.0, grid=64, slow_every=5, stall_ticks=20000,
              verbose=False):
    """Run one dish until the deepest lineage reaches ``generations`` or time runs out.

    ``stall_ticks`` stops a run that has stopped deepening: a population that survives
    without dividing can spin forever, and a 45-minute silence is not a measurement.
    """
    rng = random.Random(seed)
    dish = NutrientDish(size_m=size_m, grid=grid)
    cells = []
    for index in range(min(initial, cap)):
        x = rng.uniform(0.2, size_m - 0.2)
        y = rng.uniform(0.2, size_m - 0.2)
        cells.append(
            Cell(x, y, rng.uniform(0.0, TAU), 1.0, Genome.founding(rng), 0, index + 1)
        )
    lineages = defaultdict(set)
    buckets = {}
    ticks = 0
    max_gen = 0
    baseline = None
    extinct_after_floor = False
    stalled = False
    started = time.time()
    limit_s = minutes * 60.0
    last_depth_tick = 0

    while max_gen < generations and cells:
        if ticks % slow_every == 0:
            dish.step()
        _crowding(cells, buckets)
        children = []
        room = cap - len(cells)
        for cell in cells:
            if not cell.alive:
                continue
            cell.age += 1
            density = _neighbours(cell, buckets)
            penalty = _CROWD_COST * max(density, 0) * (1.0 - cell.genome.get("toxin_tolerance"))
            size = cell.genome.get("size")
            speed = cell.genome.get("speed")
            adhesion = cell.genome.get("adhesion")
            dormant = cell.energy < cell.genome.get("dormancy_threshold")

            eat_rate = _UPTAKE * size * (0.5 if dormant else 1.0)
            patch = dish.patch_at(cell.x, cell.y)
            eaten = dish.take(cell.x, cell.y, eat_rate)
            if eaten > 0.0 and patch >= 0:
                lineages[cell.lineage].add(patch)
            cell.energy += eaten * cell.genome.get("efficiency")

            cost = (_BASE_COST + _MOVE_COST * speed * speed * size + penalty)
            cost *= 1.0 - 0.30 * adhesion
            if dormant:
                cost *= 0.3
            cell.energy -= cost

            if not dormant:
                gx, gy = dish.gradient(cell.x, cell.y)
                vx = cell.genome.get("nutrient_affinity") * gx
                vy = cell.genome.get("nutrient_affinity") * gy
                vx += -cell.genome.get("light_affinity") * 0.5 / size_m
                vy += (
                    -cell.genome.get("temperature_affinity")
                    * (1.0 if cell.y > size_m * 0.5 else -1.0)
                    / size_m
                )
                if vx * vx + vy * vy > 1e-12:
                    target = math.atan2(vy, vx)
                    cell.heading += clamp(_wrap(target - cell.heading), -_TURN_RATE, _TURN_RATE)
                move = speed * (1.0 - 0.5 * adhesion)
                cell.x += math.cos(cell.heading) * move
                cell.y += math.sin(cell.heading) * move
                if cell.x < 0.0:
                    cell.x = 0.0
                    cell.heading = math.pi - cell.heading
                elif cell.x > size_m:
                    cell.x = size_m
                    cell.heading = math.pi - cell.heading
                if cell.y < 0.0:
                    cell.y = 0.0
                    cell.heading = -cell.heading
                elif cell.y > size_m:
                    cell.y = size_m
                    cell.heading = -cell.heading
                cell.heading = _wrap(cell.heading)

            if cell.energy <= 0.0:
                cell.alive = False
                continue

            if cell.energy >= cell.genome.get("division_threshold") and room > 0:
                cell.energy *= 0.5
                child = Cell(
                    clamp(cell.x + rng.uniform(-_CHILD_OFFSET, _CHILD_OFFSET), 0.0, size_m),
                    clamp(cell.y + rng.uniform(-_CHILD_OFFSET, _CHILD_OFFSET), 0.0, size_m),
                    rng.uniform(0.0, TAU),
                    cell.energy,
                    cell.genome.mutate(rng),
                    cell.gen + 1,
                    cell.lineage,
                )
                children.append(child)
                room -= 1

        cells = [cell for cell in cells if cell.alive]
        cells.extend(children)
        ticks += 1
        if children:
            deepest = max(child.gen for child in children)
            if deepest > max_gen:
                max_gen = deepest
                last_depth_tick = ticks
        if baseline is None and max_gen >= 100:
            baseline = _snapshot(cells, lineages, ticks)
        if verbose and ticks % 5000 == 0:
            print(
                f"  seed {seed}: tick {ticks} gen {max_gen} "
                f"pop {len(cells)} {ticks / max(time.time() - started, 1e-9):.0f} t/s",
                flush=True,
            )
        if not cells:
            if max_gen >= SURVIVAL_FLOOR_GEN:
                extinct_after_floor = True
            break
        if ticks % 200 == 0:
            if time.time() - started > limit_s:
                stalled = True
                break
            if ticks - last_depth_tick > stall_ticks:
                stalled = True
                break

    elapsed = max(time.time() - started, 1e-9)
    final = _snapshot(cells, lineages, ticks)
    return {
        "seed": seed,
        "design": "nutrient-only, no predation",
        "target_generations": generations,
        "max_gen": max_gen,
        "reached_target": max_gen >= generations,
        "extinct_after_floor": extinct_after_floor,
        "stalled": stalled,
        "ticks": ticks,
        "elapsed_s": round(elapsed, 1),
        "ticks_per_s": round(ticks / elapsed, 1),
        "population_cap": cap,
        "baseline": baseline,
        "final": final,
        "digest": stable_hash({"seed": seed, "ticks": ticks, "final": final}),
    }


def evaluate(results, target=TARGET_GENERATIONS):
    """Apply the four-part falsifier on the median of the seeds."""
    if not results:
        return {"passed": False, "checks": {}, "reason": "no results"}
    survived = all(
        row["reached_target"] and not row["extinct_after_floor"] for row in results
    )
    depths = sorted(row["final"]["median_depth"] for row in results)
    median_depth = depths[len(depths) // 2]
    depth_ok = median_depth >= SUCCESS_MEDIAN_DEPTH

    ratios = []
    for row in results:
        base = row["baseline"]["niche_breadth"] if row["baseline"] else 0.0
        final = row["final"]["niche_breadth"]
        ratios.append((final + 1.0) / (base + 1.0))
    ratios.sort()
    niche_ratio = ratios[len(ratios) // 2]
    niche_ok = niche_ratio >= SUCCESS_NICHE_GROWTH

    z_scores = {}
    if results[0]["baseline"]:
        for name in GENE_NAMES:
            base_values = [row["baseline"]["traits"].get(name, 0.0) for row in results]
            final_values = [row["final"]["traits"].get(name, 0.0) for row in results]
            base_mean = mean(base_values)
            spread = math.sqrt(mean((value - base_mean) ** 2 for value in base_values))
            z_scores[name] = round(abs(mean(final_values) - base_mean) / max(spread, 1e-9), 3)
    best_trait = max(z_scores, key=z_scores.get) if z_scores else None
    trait_ok = bool(z_scores) and z_scores[best_trait] >= SUCCESS_TRAIT_Z

    checks = {
        "survived_last_10k": survived,
        "median_depth_ge_100": {"passed": depth_ok, "median_depth": median_depth},
        "niche_breadth_doubled": {"passed": niche_ok, "ratio": round(niche_ratio, 3)},
        "trait_selection_ge_2sd": {
            "passed": trait_ok,
            "trait": best_trait,
            "z": z_scores.get(best_trait, 0.0) if best_trait else 0.0,
        },
    }
    passed = survived and depth_ok and niche_ok and trait_ok
    return {
        "passed": passed,
        "checks": checks,
        "trait_z_scores": z_scores,
        "seeds": [row["seed"] for row in results],
        "target_generations": target,
    }


def format_table(results):
    if not results:
        return "(no results)"
    header = (
        f"{'seed':<10}{'max_gen':>8}{'pop':>5}{'depth':>7}{'div':>7}"
        f"{'niche0':>7}{'niche1':>7}{'ticks':>9}{'tps':>8}{'target':>7}{'ext':>5}"
    )
    lines = [header, "-" * len(header)]
    for row in results:
        base = row["baseline"]["niche_breadth"] if row["baseline"] else 0.0
        lines.append(
            f"{row['seed']:<10}{row['max_gen']:>8}{row['final']['population']:>5}"
            f"{row['final']['median_depth']:>7}{row['final']['diversity']:>7.3f}"
            f"{base:>7.0f}{row['final']['niche_breadth']:>7.0f}"
            f"{row['ticks']:>9}{row['ticks_per_s']:>8.0f}"
            f"{str(row['reached_target']):>7}{str(row['extinct_after_floor']):>5}"
        )
    return "\n".join(lines)
