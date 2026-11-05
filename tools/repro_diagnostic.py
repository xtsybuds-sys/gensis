"""Why does reproduction never fire? Sample the gates it requires.

Prints how often each reproduction gate is satisfied during a full run, the
highest energy and nutrition ever observed, the closest pair distance, and how
often a pair was simultaneously ready and in range. This is diagnosis, not a
tuned demo: the numbers decide whether the gating is wrong or the agents cannot
reach it.
"""

from __future__ import annotations

import math

from genesis.config import Config
from genesis.sim import Simulation


def main():
    cfg = Config(
        seed=20261105,
        days=5.0,
        grid=32,
        population=5,
        log_every=0,
        checkpoint_every=0,
    )
    sim = Simulation(cfg)
    sample_ticks = 900

    samples = 0
    alive_total = 0
    energy_ok = nutrition_ok = cooldown_ok = all_ok = 0
    max_energy = 0.0
    max_nutrition = 0.0
    min_pair = float("inf")
    ready_pairs_in_range = 0

    for tick in range(cfg.tick_count):
        sim.step()
        if (tick + 1) % sample_ticks and tick != cfg.tick_count - 1:
            continue
        alive = [a for a in sim.agents if a.alive]
        if not alive:
            break
        samples += 1
        alive_total += len(alive)
        max_energy = max([max_energy] + [a.energy for a in alive])
        max_nutrition = max([max_nutrition] + [a.nutrition for a in alive])
        energy_ok += sum(1 for a in alive if a.energy >= cfg.reproduction_min_energy)
        nutrition_ok += sum(
            1 for a in alive if a.nutrition >= cfg.reproduction_min_nutrition
        )
        cooldown_ok += sum(1 for a in alive if a.cooldown_s <= 0.0)
        ready = [
            a
            for a in alive
            if a.cooldown_s <= 0.0
            and a.energy >= cfg.reproduction_min_energy
            and a.nutrition >= cfg.reproduction_min_nutrition
        ]
        all_ok += len(ready)
        for i in range(len(alive)):
            for j in range(i + 1, len(alive)):
                dx = alive[i].pos[0] - alive[j].pos[0]
                dy = alive[i].pos[1] - alive[j].pos[1]
                min_pair = min(min_pair, math.hypot(dx, dy))
        for i in range(len(ready)):
            for j in range(i + 1, len(ready)):
                dx = ready[i].pos[0] - ready[j].pos[0]
                dy = ready[i].pos[1] - ready[j].pos[1]
                if math.hypot(dx, dy) <= cfg.reproduction_range_m:
                    ready_pairs_in_range += 1

    per = max(alive_total, 1)
    print(
        "samples=%d alive_per_sample=%.2f gates: energy=%d nutrition=%d cooldown=%d all=%d"
        % (samples, alive_total / max(samples, 1), energy_ok, nutrition_ok,
           cooldown_ok, all_ok)
    )
    print(
        "share_of_samples: energy=%.3f nutrition=%.3f all=%.3f"
        % (energy_ok / per, nutrition_ok / per, all_ok / per)
    )
    print(
        "max_energy=%.3f max_nutrition=%.3f min_pair_m=%.2f ready_pairs_in_range=%d"
        % (max_energy, max_nutrition, min_pair, ready_pairs_in_range)
    )
    print(
        "births=%d deaths=%d observed_days=%.2f range_m=%.1f cooldown_s=%.0f"
        % (
            sim.births,
            sim.deaths,
            max((a.age_s for a in sim.agents), default=0.0) / 86400.0,
            cfg.reproduction_range_m,
            cfg.reproduction_cooldown_s,
        )
    )


if __name__ == "__main__":
    main()
