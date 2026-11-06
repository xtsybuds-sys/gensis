"""Live protocell feed for the world viewer.

The feed runs the real ``ProtocellReactor``; it does not reimplement the chemistry. It
starts from a warm chemistry state (the simulation is advanced before serving) so the
viewer does not open on empty water, but nothing is placed: every vesicle is descended
from the t=0 monomers.

The reactor is well-mixed, so vesicle positions here are presentation-only. They are
spread for visibility and are not used by the chemistry or by selection.
"""

from __future__ import annotations

import random
import threading
import time

from .protocell import DIVIDE_LIPIDS, ProtocellReactor


class ProtocellLiveFeed:
    """A continuously stepping protocell reactor with a thread-safe latest frame."""

    def __init__(self, seed=20261105, warmup_ticks=2000, ticks_per_second=20.0,
                 size_m=16.0):
        self.seed = int(seed)
        self.warmup_ticks = int(warmup_ticks)
        self.ticks_per_second = float(ticks_per_second)
        self.size_m = float(size_m)
        self.reactor = ProtocellReactor(self.seed)
        self._position_rng = random.Random(self.seed ^ 0x9E3779B9)
        self._positions: dict[int, tuple[float, float]] = {}
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread = None
        self.error = None
        self.started_at = time.time()
        self._next_tick_at = time.perf_counter()
        for _ in range(max(0, self.warmup_ticks)):
            self.reactor.step()
        self._frame = self._build_frame()

    def start(self):
        if self._thread is not None:
            return
        self._thread = threading.Thread(target=self._run, name="genesis-protocell",
                                        daemon=True)
        self._thread.start()

    def stop(self):
        self._stop.set()

    def snapshot(self):
        with self._lock:
            return dict(self._frame)

    def _run(self):
        try:
            while not self._stop.is_set():
                started = time.perf_counter()
                with self._lock:
                    self.reactor.step()
                    self._frame = self._build_frame()
                if self.ticks_per_second > 0:
                    delay = (1.0 / self.ticks_per_second) - (time.perf_counter() - started)
                    if delay > 0:
                        time.sleep(delay)
        except Exception as exc:  # keep the viewer honest about failures
            with self._lock:
                self.error = f"{type(exc).__name__}: {exc}"

    def _build_frame(self):
        vesicles = list(self.reactor.vesicles)
        alive = set()
        cells = []
        for vesicle in vesicles:
            key = id(vesicle)
            alive.add(key)
            position = self._positions.get(key)
            if position is None:
                position = (
                    self._position_rng.uniform(1.0, 15.0),
                    self._position_rng.uniform(1.0, 15.0),
                )
                self._positions[key] = position
            cells.append([
                round(position[0], 2),
                round(position[1], 2),
                round(min(1.5, max(0.4, vesicle.lipids / DIVIDE_LIPIDS)), 2),
                round(min(vesicle.catalyst_total, 4.0), 2),
                int(vesicle.lineage),
                int(vesicle.total),
            ])
        self._positions = {key: value for key, value in self._positions.items()
                           if key in alive}
        count = max(len(vesicles), 1)
        return {
            "tick": self.reactor.tick,
            "births": self.reactor.births,
            "turnovers": self.reactor.births,
            "population": len(vesicles),
            "max_gen": max((vesicle.generation for vesicle in vesicles), default=0),
            "mean_energy": round(sum(vesicle.catalyst_total for vesicle in vesicles)
                                 / count, 3),
            "mean_size": round(sum(vesicle.lipids for vesicle in vesicles) / count, 3),
            "mean_speed": round(sum(vesicle.total for vesicle in vesicles) / count, 1),
            "lineages": len({vesicle.lineage for vesicle in vesicles}),
            "cells": cells,
            "size_m": self.size_m,
            "mode": "protocell",
            "first_catalyst_tick": self.reactor.first_catalyst_tick,
            "first_replication_tick": self.reactor.first_replication_tick,
            "mutations": self.reactor.mutations,
            "divisions": self.reactor.divisions,
            "position_note": "presentation only; the reactor is well-mixed",
            "wall_time": time.time(),
        }
