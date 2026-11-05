"""Multi-seed experiment harness: calibration, ablations, validity floor.

The harness exists so no claim rests on one lucky run. Every arm is run on the
same seeds and the same generated worlds; the only difference is the factor under
test (architecture, planner, or a random-policy control).
"""

from __future__ import annotations

import time

from .brains.baseline import RandomPolicy
from .config import Config
from .sim import Simulation

ARMS = ("population", "random", "no_planner")


def _override_for(arm):
    if arm == "random":
        return lambda kind, rng, cfg, label: RandomPolicy(rng, label=label)
    return None


def run_variant(seed, days=5.0, arm="population", planner=True, grid=32,
                population=5, world=1024):
    cfg = Config(
        seed=seed,
        days=days,
        grid=grid,
        population=population,
        world_size_m=world,
        planner=planner,
        checkpoint_every=0,
        log_every=360,
    )
    sim = Simulation(cfg, None, brain_override=_override_for(arm))
    started = time.time()
    for _ in range(cfg.tick_count):
        sim.step()
    elapsed = max(time.time() - started, 1e-9)
    alive = [a for a in sim.agents if a.alive]
    death_ages = [a.age_s for a in sim.agents if not a.alive]
    oldest = max((a.age_s for a in sim.agents), default=0.0)
    total_decisions = sim.decisions + sim.skipped_decisions
    return {
        "seed": seed,
        "arm": arm,
        "world_m": world,
        "planner": planner,
        "days": round(days, 3),
        "ticks": sim.tick,
        "elapsed_s": round(elapsed, 1),
        "ticks_per_s": round(sim.tick / elapsed, 1),
        "survivors": len(alive),
        "population_end": len(sim.agents),
        "births": sim.births,
        "max_generation": max((a.generation for a in sim.agents), default=0),
        "first_death_day": round(min(death_ages) / 86400.0, 2) if death_ages else None,
        "observed_days": round(oldest / 86400.0, 2),
        "first_drink_day": (
            None
            if sim.first_drink is None
            else round(sim.first_drink["tick"] * cfg.tick_seconds / 86400.0, 2)
        ),
        "first_drink_distance_m": (
            None if sim.first_drink is None else sim.first_drink["distance_m"]
        ),
        "discoveries": len(sim.discoveries),
        "encounters": sim.encounters,
        "transfers": len(sim.knowledge_links),
        "mean_prediction_error": (
            round(sum(a.brain.prediction_error for a in alive) / len(alive), 5)
            if alive
            else None
        ),
        "sleep_skipped_fraction": (
            round(sim.skipped_decisions / total_decisions, 3)
            if total_decisions
            else 0.0
        ),
        "dream_replays": sim.dream_replays,
    }


def calibrate(seeds, days=5.0, arms=ARMS, grid=32, population=5, world=1024):
    results = []
    for arm in arms:
        planner = arm != "no_planner"
        real_arm = "population" if arm == "no_planner" else arm
        for seed in seeds:
            results.append(
                run_variant(
                    seed,
                    days=days,
                    arm=real_arm,
                    planner=planner,
                    grid=grid,
                    population=population,
                    world=world,
                )
            )
    return results


COLUMNS = (
    "arm",
    "world_m",
    "seed",
    "survivors",
    "observed_days",
    "first_death_day",
    "first_drink_day",
    "first_drink_distance_m",
    "births",
    "max_generation",
    "sleep_skipped_fraction",
    "ticks_per_s",
)


def format_table(results):
    if not results:
        return "(no results)"
    rows = [[str(r.get(column)) for column in COLUMNS] for r in results]
    widths = [
        max([len(column)] + [len(row[i]) for row in rows])
        for i, column in enumerate(COLUMNS)
    ]
    lines = ["  ".join(column.ljust(widths[i]) for i, column in enumerate(COLUMNS))]
    lines.append("  ".join("-" * width for width in widths))
    for row in rows:
        lines.append("  ".join(value.ljust(widths[i]) for i, value in enumerate(row)))
    return "\n".join(lines)
