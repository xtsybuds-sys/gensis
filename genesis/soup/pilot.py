"""The primordial soup pilot: cells compete for nutrients, mutate, and reproduce.

Design approved by Muse (2026-11-05), nutrient-only. The pilot answers one question:
does measurable complexity grow from mutation plus selection on a simple substrate?

Two corrections from the 2,000-lineage-depth run (Muse, 2026-11-05):
- the generation clock is population-normalised births (turnovers), because the old
  deepest-chain counter froze whenever the dominant lineage died;
- niche specialisation is per-lineage patch-share entropy, because patch count hits the
  three-patch ceiling at generation 100 and could never halve.
"""

from __future__ import annotations

import json
import math
import os
import random
import time
from collections import defaultdict

from ..util import TAU, clamp, mean, stable_hash
from .dish import PATCH_CENTRES, NutrientDish
from .genome import GENE_NAMES, GENES, Genome

TARGET_TURNOVERS = 2000
SURVIVAL_FLOOR_TURNOVERS = 1000
SUCCESS_MEDIAN_DEPTH = 100
SUCCESS_ENTROPY_FACTOR = 0.5
SUCCESS_TRAIT_Z = 2.0
PATCH_COUNT = len(PATCH_CENTRES)

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


def _lineage_entropy(shares):
    """Normalized Shannon entropy of a lineage's feeding share: 1 = all patches, 0 = one."""
    total = sum(shares.values())
    if total <= 0.0:
        return 0.0
    entropy = 0.0
    for value in shares.values():
        if value > 0.0:
            p = value / total
            entropy -= p * math.log(p)
    return entropy / math.log(PATCH_COUNT)


def _snapshot(cells, lineages, ticks, births=0, mean_pop=1.0):
    if not cells:
        return {
            "population": 0,
            "median_depth": 0,
            "max_depth": 0,
            "diversity": 0.0,
            "niche_breadth": 0.0,
            "niche_entropy": 0.0,
            "lineages": 0,
            "top_lineages": [],
            "births": births,
            "turnovers": round(births / max(mean_pop, 1e-9), 3),
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
    # Niche specialisation is measured per lineage and reported as a median: a
    # population-wide count saturates at the patch ceiling immediately.
    present = {}
    lineage_gens = {}
    for cell in cells:
        present[cell.lineage] = present.get(cell.lineage, 0) + 1
        lineage_gens.setdefault(cell.lineage, []).append(cell.gen)
    entropies = sorted(_lineage_entropy(lineages[lineage]) for lineage in present)
    breadths = sorted(
        sum(1 for value in lineages[lineage].values() if value > 0.0)
        for lineage in present
    )
    lineage_rows = []
    for lineage, count in present.items():
        gens = sorted(lineage_gens[lineage])
        shares = lineages[lineage]
        lineage_rows.append(
            {
                "lineage": lineage,
                "cells": count,
                "patches": sum(1 for value in shares.values() if value > 0.0),
                "entropy": round(_lineage_entropy(shares), 4),
                "median_gen": gens[len(gens) // 2],
            }
        )
    lineage_rows.sort(key=lambda row: (-row["cells"], row["lineage"]))
    traits = {
        name: round(mean(cell.genome.values[i] for cell in cells), 6)
        for i, name in enumerate(GENE_NAMES)
    }
    middle = len(entropies) // 2
    return {
        "population": len(cells),
        "median_depth": depths[len(depths) // 2],
        "max_depth": depths[-1],
        "diversity": round(total / pairs, 6) if pairs else 0.0,
        "niche_breadth": float(breadths[len(breadths) // 2]) if breadths else 0.0,
        "niche_entropy": round(entropies[middle], 4) if entropies else 0.0,
        "lineages": len(present),
        "top_lineages": lineage_rows[:10],
        "births": births,
        "turnovers": round(births / max(mean_pop, 1e-9), 3),
        "traits": traits,
        "ticks": ticks,
    }


def _result(seed, target_turnovers, floor_turnovers, turnovers, max_gen, cells,
            lineages, ticks, births, elapsed, cap, baseline, extinct_after_floor,
            stalled, mean_pop, partial=False):
    """Assemble one run row; the same shape is used for checkpoints and final output."""
    final = _snapshot(cells, lineages, ticks, births, mean_pop)
    return {
        "seed": seed,
        "design": "nutrient-only, no predation",
        "clock": "turnovers (births / mean population)",
        "target_turnovers": target_turnovers,
        "floor_turnovers": floor_turnovers,
        "turnovers": round(turnovers, 2),
        "max_gen": max_gen,
        "reached_target": turnovers >= target_turnovers,
        "extinct_after_floor": extinct_after_floor,
        "stalled": stalled,
        "partial": partial,
        "ticks": ticks,
        "births": births,
        "elapsed_s": round(elapsed, 1),
        "ticks_per_s": round(ticks / max(elapsed, 1e-9), 1),
        "population_cap": cap,
        "baseline": baseline,
        "final": final,
        "digest": stable_hash({"seed": seed, "ticks": ticks, "final": final}),
    }


def _write_checkpoint(path, row):
    """Write a partial row atomically, so a killed run still leaves usable numbers."""
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as handle:
        json.dump({"rows": [row], "partial": True}, handle, indent=2)
    os.replace(tmp, path)


def run_pilot(seed, target_turnovers=TARGET_TURNOVERS, minutes=45.0, initial=200,
              cap=600, size_m=16.0, grid=64, slow_every=5, stall_ticks=20000,
              verbose=False, floor_turnovers=SURVIVAL_FLOOR_TURNOVERS,
              checkpoint_path=None, checkpoint_every=100, on_tick=None):
    """Run one dish until population-normalised births reach the target or time runs out.

    Turnovers are cumulative births divided by mean population, so the clock cannot
    freeze when a lineage dies. ``stall_ticks`` stops a dish that produces no births at
    all for that many ticks; that guard is now based on the same clock as the target.
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
    lineages = defaultdict(dict)
    buckets = {}
    ticks = 0
    births = 0
    pop_sum = 0
    turnovers = 0.0
    max_gen = 0
    last_birth_tick = 0
    baseline = None
    extinct_after_floor = False
    stalled = False
    started = time.time()
    limit_s = minutes * 60.0
    last_checkpoint = 0

    while turnovers < target_turnovers and cells:
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
                shares = lineages[cell.lineage]
                shares[patch] = shares.get(patch, 0.0) + eaten
            cell.energy += eaten * cell.genome.get("efficiency")

            cost = _BASE_COST + _MOVE_COST * speed * speed * size + penalty
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
                births += 1
                room -= 1

        cells = [cell for cell in cells if cell.alive]
        cells.extend(children)
        ticks += 1
        pop_sum += len(cells)
        mean_pop = pop_sum / ticks
        turnovers = births / max(mean_pop, 1e-9)
        if children:
            deepest = max(child.gen for child in children)
            if deepest > max_gen:
                max_gen = deepest
            last_birth_tick = ticks
        if baseline is None and turnovers >= 100.0:
            baseline = _snapshot(cells, lineages, ticks, births, mean_pop)
        if on_tick is not None and on_tick(dish, cells, ticks, births, max_gen) is False:
            break
        if checkpoint_path and turnovers >= last_checkpoint + checkpoint_every:
            last_checkpoint = int(turnovers // checkpoint_every) * checkpoint_every
            _write_checkpoint(
                checkpoint_path,
                _result(
                    seed, target_turnovers, floor_turnovers, turnovers, max_gen,
                    cells, lineages, ticks, births, time.time() - started, cap,
                    baseline, extinct_after_floor, stalled, mean_pop, partial=True,
                ),
            )
        if verbose and ticks % 5000 == 0:
            print(
                f"  seed {seed}: tick {ticks} turnovers {turnovers:.0f} gen {max_gen} "
                f"pop {len(cells)} {ticks / max(time.time() - started, 1e-9):.0f} t/s",
                flush=True,
            )
        if not cells:
            if turnovers >= floor_turnovers:
                extinct_after_floor = True
            break
        if ticks % 200 == 0:
            if time.time() - started > limit_s:
                stalled = True
                break
            if ticks - last_birth_tick > stall_ticks:
                stalled = True
                break

    elapsed = max(time.time() - started, 1e-9)
    mean_pop = pop_sum / max(ticks, 1)
    return _result(
        seed, target_turnovers, floor_turnovers, turnovers, max_gen, cells,
        lineages, ticks, births, elapsed, cap, baseline, extinct_after_floor,
        stalled, mean_pop,
    )


def evaluate(results, target=TARGET_TURNOVERS):
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
    baseline_entropies = []
    for row in results:
        base = (row["baseline"] or {}).get("niche_entropy")
        baseline_entropies.append(base)
        if base is None or base <= 1e-9:
            ratios.append(None)
        else:
            ratios.append(row["final"]["niche_entropy"] / base)
    valid = [ratio for ratio in ratios if ratio is not None]
    median_ratio = sorted(valid)[len(valid) // 2] if valid else None
    entropy_ok = (
        median_ratio is not None and len(valid) == len(ratios)
        and median_ratio <= SUCCESS_ENTROPY_FACTOR
    )

    z_scores = {}
    if results[0]["baseline"]:
        widths = {name: high - low for name, low, high, _ in GENES}
        for name in GENE_NAMES:
            base_values = [row["baseline"]["traits"].get(name, 0.0) for row in results]
            final_values = [row["final"]["traits"].get(name, 0.0) for row in results]
            base_mean = mean(base_values)
            spread = math.sqrt(mean((value - base_mean) ** 2 for value in base_values))
            spread = max(spread, 0.05 * widths.get(name, 1.0))
            z_scores[name] = round(abs(mean(final_values) - base_mean) / spread, 3)
    best_trait = max(z_scores, key=z_scores.get) if z_scores else None
    trait_ok = bool(z_scores) and z_scores[best_trait] >= SUCCESS_TRAIT_Z

    checks = {
        "survived_after_floor": survived,
        "median_depth_ge_100": {"passed": depth_ok, "median_depth": median_depth},
        "entropy_halved": {
            "passed": entropy_ok,
            "median_ratio": round(median_ratio, 3) if median_ratio is not None else None,
            "baseline_entropies": baseline_entropies,
            "final_entropies": [row["final"]["niche_entropy"] for row in results],
        },
        "trait_selection_ge_2sd": {
            "passed": trait_ok,
            "trait": best_trait,
            "z": z_scores.get(best_trait, 0.0) if best_trait else 0.0,
        },
    }
    passed = survived and depth_ok and entropy_ok and trait_ok
    return {
        "passed": passed,
        "checks": checks,
        "trait_z_scores": z_scores,
        "seeds": [row["seed"] for row in results],
        "target_turnovers": target,
    }


def format_table(results):
    if not results:
        return "(no results)"
    header = (
        f"{'seed':<10}{'turn':>7}{'gen':>6}{'pop':>5}{'depth':>7}{'div':>7}"
        f"{'H0':>7}{'H1':>7}{'lin':>5}{'ticks':>9}{'tps':>8}{'target':>8}{'ext':>5}"
    )
    lines = [header, "-" * len(header)]
    for row in results:
        base = (row["baseline"] or {}).get("niche_entropy", 0.0)
        lines.append(
            f"{row['seed']:<10}{row['turnovers']:>7.0f}{row['max_gen']:>6}"
            f"{row['final']['population']:>5}{row['final']['median_depth']:>7}"
            f"{row['final']['diversity']:>7.3f}{base:>7.3f}"
            f"{row['final']['niche_entropy']:>7.3f}{row['final']['lineages']:>5}"
            f"{row['ticks']:>9}{row['ticks_per_s']:>8.0f}"
            f"{str(row['reached_target']):>8}{str(row['extinct_after_floor']):>5}"
        )
    return "\n".join(lines)
