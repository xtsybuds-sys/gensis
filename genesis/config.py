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
    """

    seed: int = 20261105
    days: float = 5.0
    tick_seconds: float = 10.0
    decision_every: int = 5
    sense_every: int = 5
    slow_every: int = 6
    grid: int = 32
    world_size_m: float = 1024.0
    population: int = 5
    water_level_m: float = 11.0
    checkpoint_every: int = 720
    log_every: int = 360
    max_ticks: int | None = None
    novelty_weight: float = 0.35
    plasticity: float = 0.02
    hidden_units: int = 24

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
