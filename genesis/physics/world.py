"""The assembled physical world and its multiscale update schedule."""

from __future__ import annotations

import math

from ..util import TAU, clamp
from .fields import HydrostaticWater, Plants, ThermalField
from .terrain import generate_terrain

SECONDS_PER_DAY = 86400.0


class PhysicsWorld:
    def __init__(self, cfg, rng):
        self.cfg = cfg
        self.terrain = generate_terrain(cfg.grid, cfg.world_size_m, rng)
        n = cfg.grid
        level = cfg.water_level_m
        depth = [
            [max(0.0, level - self.terrain.heights[j][i]) for i in range(n)]
            for j in range(n)
        ]
        self.water = HydrostaticWater(self.terrain, depth)
        self.thermal = ThermalField(self.terrain)
        self.plants = Plants(self.terrain, rng)
        self.time_s = 0.0
        self.slow_updates = 0
        cell_area = self.terrain.cell_m ** 2
        self.initial_water_m3 = self.water.volume(cell_area)
        self.initial_thermal_energy = self.thermal.total_energy()

    # -- solar / time -----------------------------------------------------
    def day_phase(self, time_s=None):
        t = self.time_s if time_s is None else time_s
        return (t % SECONDS_PER_DAY) / SECONDS_PER_DAY

    def sun_elevation(self, time_s=None):
        return math.sin(TAU * (self.day_phase(time_s) - 0.25))

    def light(self, time_s=None):
        return clamp((self.sun_elevation(time_s) + 0.10) / 1.10, 0.0, 1.0)

    def clock(self):
        phase = self.day_phase()
        hours = phase * 24.0
        return f"day {int(self.time_s // SECONDS_PER_DAY) + 1} {int(hours):02d}:{int((hours % 1) * 60):02d}"

    # -- stepping ---------------------------------------------------------
    def step(self, dt, tick):
        self.time_s += dt
        if tick % self.cfg.slow_every == 0:
            self.slow_updates += 1
            self.water.step(sweeps=2)
            light = self.light()
            self.thermal.step(self.cfg.slow_dt, light, self.water.depth)
            self.plants.step(
                self.cfg.slow_dt, light, self.thermal.mean(), self.water.depth
            )

    # -- field lookups ----------------------------------------------------
    def _bilinear(self, grid, x, y):
        n = self.cfg.grid
        cell = self.terrain.cell_m
        gx = clamp(x / cell, 0.0, n - 1.000001)
        gy = clamp(y / cell, 0.0, n - 1.000001)
        i = int(gx)
        j = int(gy)
        tx = gx - i
        ty = gy - j
        v00 = grid[j][i]
        v10 = grid[j][i + 1]
        v01 = grid[j + 1][i]
        v11 = grid[j + 1][i + 1]
        top = v00 + (v10 - v00) * tx
        bottom = v01 + (v11 - v01) * tx
        return top + (bottom - top) * ty

    def water_depth_at(self, x, y):
        return self._bilinear(self.water.depth, x, y)

    def biomass_at(self, x, y):
        return self._bilinear(self.plants.biomass, x, y)

    def temperature_at(self, x, y):
        return self._bilinear(self.thermal.temp, x, y)

    # -- reporting --------------------------------------------------------
    def conservation(self):
        cell_area = self.terrain.cell_m ** 2
        water_now = self.water.volume(cell_area)
        thermal_now = self.thermal.total_energy()
        thermal_expected = (
            self.initial_thermal_energy
            + self.thermal.injected
            - self.thermal.radiated
            + self.thermal.capacity_adjustment
        )
        return {
            "water_start_m3": round(self.initial_water_m3, 3),
            "water_now_m3": round(water_now, 3),
            "water_drift_m3": round(water_now - self.initial_water_m3, 6),
            "thermal_energy_start": round(self.initial_thermal_energy, 6),
            "thermal_energy_now": round(thermal_now, 6),
            "thermal_energy_expected": round(thermal_expected, 6),
            "thermal_residual": round(thermal_now - thermal_expected, 6),
        }

    # -- persistence ------------------------------------------------------
    def state(self):
        return {
            "terrain": self.terrain.heights,
            "depth": self.water.depth,
            "temp": self.thermal.temp,
            "capacity": self.thermal.capacity,
            "biomass": self.plants.biomass,
            "plant_capacity": self.plants.capacity,
            "time_s": self.time_s,
            "slow_updates": self.slow_updates,
            "injected": self.thermal.injected,
            "radiated": self.thermal.radiated,
            "capacity_adjustment": self.thermal.capacity_adjustment,
            "initial_water_m3": self.initial_water_m3,
            "initial_thermal_energy": self.initial_thermal_energy,
        }

    def load_state(self, data):
        self.terrain.heights = data["terrain"]
        self.water.depth = data["depth"]
        self.thermal.temp = data["temp"]
        self.thermal.capacity = data["capacity"]
        self.plants.biomass = data["biomass"]
        self.plants.capacity = data["plant_capacity"]
        self.time_s = data["time_s"]
        self.slow_updates = data["slow_updates"]
        self.thermal.injected = data["injected"]
        self.thermal.radiated = data["radiated"]
        self.thermal.capacity_adjustment = data["capacity_adjustment"]
        self.initial_water_m3 = data["initial_water_m3"]
        self.initial_thermal_energy = data["initial_thermal_energy"]

    def summary(self):
        tmin, tmax = self.thermal.bounds()
        return {
            "time_s": round(self.time_s, 1),
            "clock": self.clock(),
            "light": round(self.light(), 4),
            "sun_elevation": round(self.sun_elevation(), 4),
            "terrain": self.terrain.summary(),
            "water_m3": round(self.water.volume(self.terrain.cell_m ** 2), 1),
            "biomass": round(self.plants.total(), 2),
            "temperature_c": [round(tmin, 2), round(self.thermal.mean(), 2), round(tmax, 2)],
            "slow_updates": self.slow_updates,
        }
