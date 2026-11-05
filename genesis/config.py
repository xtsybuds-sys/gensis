from __future__ import annotations

from dataclasses import asdict, dataclass, replace

SECONDS_PER_DAY = 86400.0


@dataclass(frozen=True)
class Config:
    """Tunable simulation parameters.

    One tick is ``tick_seconds`` of world time. Slow physical fields (water,
    heat, vegetation) update every ``slow_every`` ticks, which is the
    multiscale seam: cheap global processes run coarsely, while the
    high-fidelity solvers are reserved for local experiments.

    ``start_hour`` exists because a life that begins at midnight spends most of
    its decision slots asleep (measured: 51-99% skipped). Lives start at dawn so
    the calibration measures decisions rather than sleep. It is a calibration
    fix, not a tune-away: the sleep/dream mechanism itself is unchanged.

    The ``shaping_*`` and ``drive_*`` weights define the dense reward described
    in the calibration sprint: immediate physiological change plus a
    potential-based term on *sensed* water/food proximity. The potential term is
    built only from the inhabitant's own sensor vector, so it adds no information
    the inhabitant does not already have (Ng et al. potential-based shaping).
    """

    seed: int = 20261105
    days: float = 5.0
    tick_seconds: float = 10.0
    decision_every: int = 5
    sense_every: int = 5
    slow_every: int = 6
    grid: int = 32
    world_size_m: float = 128.0
    start_hour: float = 6.0
    population: int = 5
    water_level_m: float = 11.0
    checkpoint_every: int = 720
    log_every: int = 360
    max_ticks: int | None = None
    novelty_weight: float = 0.35
    plasticity: float = 0.02
    hidden_units: int = 24
    planner: bool = True
    max_population: int = 12
    reproduction_min_energy: float = 0.55
    reproduction_min_nutrition: float = 0.45
    reproduction_cooldown_s: float = 43200.0
    reproduction_range_m: float = 12.0
    mutation_rate: float = 1.0
    dream_every: int = 12
    # Diagnostic ablation only: the rest action is zeroed, so no inhabitant can
    # fall asleep. Used to test whether sleep is the reason the learned arms starve
    # of decisions; not an architecture change.
    sleep_enabled: bool = True

    # Dense shaping (calibration sprint, decision 1 + work order step 1).
    shaping_hydration: float = 12.0
    shaping_energy: float = 6.0
    shaping_nutrition: float = 4.0
    shaping_approach: float = 2.5
    shaping_social: float = 1.5
    drive_thirst: float = 0.35
    drive_hunger: float = 0.20

    # Social drive (decision 4a): homeostatic, like thirst, never lethal.
    social_range_m: float = 15.0
    isolation_rise_per_day: float = 0.75
    isolation_relief_per_day: float = 2.5

    @property
    def cell_m(self) -> float:
        return self.world_size_m / self.grid

    @property
    def slow_dt(self) -> float:
        return self.slow_every * self.tick_seconds

    @property
    def tick_count(self) -> int:
        full = int(round(self.days * SECONDS_PER_DAY / self.tick_seconds))
        return full if self.max_ticks is None else min(full, self.max_ticks)

    @property
    def world_days(self) -> float:
        return self.tick_count * self.tick_seconds / SECONDS_PER_DAY

    def with_(self, **kw) -> "Config":
        return replace(self, **kw)

    def to_dict(self) -> dict:
        return asdict(self)
