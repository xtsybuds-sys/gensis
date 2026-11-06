"""Live dish feed: the real pilot stepping continuously for the world viewer.

The feed does not reimplement the simulation. It runs ``run_pilot`` unchanged and
publishes a lightweight frame from the ``on_tick`` hook, so what the viewer draws is
the same code path the falsifier measures.
"""

from __future__ import annotations

import threading
import time

from ..util import mean
from .pilot import run_pilot

_GRID = 16


class LiveFeed:
    """A continuously stepping dish with a thread-safe latest frame."""

    def __init__(self, seed=20261105, initial=200, cap=600, size_m=16.0, grid=64,
                 ticks_per_second=60.0):
        self.seed = int(seed)
        self.initial = int(initial)
        self.cap = int(cap)
        self.size_m = float(size_m)
        self.grid = int(grid)
        self.ticks_per_second = float(ticks_per_second)
        self._next_tick_at = time.perf_counter()
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread = None
        self._ticks = 0
        self._pop_sum = 0
        self.error = None
        self.started_at = time.time()
        self.frame = {
            "tick": 0,
            "births": 0,
            "turnovers": 0.0,
            "population": 0,
            "max_gen": 0,
            "mean_energy": 0.0,
            "mean_size": 0.0,
            "mean_speed": 0.0,
            "lineages": 0,
            "cells": [],
            "nutrient": [0] * (_GRID * _GRID),
            "size_m": self.size_m,
            "wall_time": time.time(),
        }

    def start(self):
        if self._thread is not None:
            return
        self._thread = threading.Thread(target=self._run, name="genesis-live", daemon=True)
        self._thread.start()

    def stop(self):
        self._stop.set()

    def snapshot(self):
        with self._lock:
            return dict(self.frame)

    def _run(self):
        try:
            run_pilot(
                self.seed,
                target_turnovers=10**9,
                minutes=10**9,
                initial=self.initial,
                cap=self.cap,
                size_m=self.size_m,
                grid=self.grid,
                verbose=False,
                on_tick=self._publish,
            )
        except Exception as exc:  # keep the viewer honest about failures
            with self._lock:
                self.error = f"{type(exc).__name__}: {exc}"

    def _publish(self, dish, cells, ticks, births, max_gen):
        if self._stop.is_set():
            return False
        if self.ticks_per_second > 0.0:
            interval = 1.0 / self.ticks_per_second
            now = time.perf_counter()
            if self._next_tick_at > now:
                time.sleep(self._next_tick_at - now)
            self._next_tick_at = max(self._next_tick_at + interval, time.perf_counter())
        self._ticks = ticks
        self._pop_sum += len(cells)
        mean_pop = max(self._pop_sum / max(ticks, 1), 1e-9)
        # Coarse nutrient field for the map view: one sample per block.
        block = dish.grid // _GRID
        nutrient = []
        for j in range(_GRID):
            for i in range(_GRID):
                value = dish.values[(j * block + block // 2) * dish.grid + (i * block + block // 2)]
                nutrient.append(int(round(value * 100)))
        body = {
            "tick": ticks,
            "births": births,
            "turnovers": round(births / mean_pop, 2),
            "population": len(cells),
            "max_gen": max_gen,
            "mean_energy": round(mean(cell.energy for cell in cells), 3),
            "mean_size": round(mean(cell.genome.get("size") for cell in cells), 3),
            "mean_speed": round(mean(cell.genome.get("speed") for cell in cells), 4),
            "lineages": len({cell.lineage for cell in cells}),
            "cells": [
                [
                    round(cell.x, 2),
                    round(cell.y, 2),
                    round(cell.genome.get("size"), 2),
                    round(min(cell.energy, 4.0), 2),
                    int(cell.lineage),
                    round(cell.genome.get("speed"), 3),
                ]
                for cell in cells[:400]
            ],
            "nutrient": nutrient,
            "size_m": dish.size_m,
            "wall_time": time.time(),
        }
        with self._lock:
            self.frame = body
        return True
