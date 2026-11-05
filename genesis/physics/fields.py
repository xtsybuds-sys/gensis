"""Fluid, thermal and vegetation fields.

Two water solvers exist on purpose, to make the multiscale seam explicit:

* :class:`ShallowWater` - explicit-flux shallow water with momentum and
  gravity. CFL limited, so it is only used for small local experiments.
* :class:`HydrostaticWater` - diffusive surface relaxation. Unconditionally
  stable at coarse timesteps, used for the persistent global world. It
  conserves water mass exactly and dissipates energy, but it carries no
  momentum, so it does not reproduce waves or hydraulic jumps.
"""

from __future__ import annotations

import math

from ..util import clamp

GRAVITY = 9.81


class ShallowWater:
    """Explicit-flux shallow water (high fidelity, small domains only)."""

    def __init__(self, terrain, depth=None, friction=0.05):
        self.terrain = terrain
        n = terrain.n
        self.n = n
        if depth is None:
            depth = [[0.0] * n for _ in range(n)]
        self.depth = depth
        self.u = [[0.0] * n for _ in range(n)]
        self.v = [[0.0] * n for _ in range(n)]
        self.friction = friction
        self.dissipated = 0.0
        self.dt_limit = 0.4 * terrain.cell_m / math.sqrt(
            GRAVITY * max(1.0, self.max_depth())
        )

    def max_depth(self):
        return max((max(row) for row in self.depth), default=0.0)

    def volume(self, cell_area=1.0):
        return sum(map(sum, self.depth)) * cell_area

    def step(self, dt):
        dt = min(dt, self.dt_limit)
        n = self.n
        t = self.terrain
        h = self.depth
        u = self.u
        v = self.v
        g = GRAVITY
        dx = t.cell_m
        damp = max(0.0, 1.0 - self.friction * dt)

        # Pressure gradient on x edges (free surface = bed + depth).
        for j in range(n):
            hj = h[j]
            uj = u[j]
            bed = t.heights[j]
            for i in range(n - 1):
                hl = hj[i]
                hr = hj[i + 1]
                if hl <= 1e-9 and hr <= 1e-9:
                    uj[i] = 0.0
                    continue
                eta_l = bed[i] + hl
                eta_r = bed[i + 1] + hr
                uj[i] = (uj[i] - g * dt / dx * (eta_r - eta_l)) * damp

        # Pressure gradient on y edges.
        for j in range(n - 1):
            for i in range(n):
                hl = h[j][i]
                hr = h[j + 1][i]
                if hl <= 1e-9 and hr <= 1e-9:
                    v[j][i] = 0.0
                    continue
                eta_l = t.heights[j][i] + hl
                eta_r = t.heights[j + 1][i] + hr
                v[j][i] = (v[j][i] - g * dt / dx * (eta_r - eta_l)) * damp

        # Conservative transport of mass between neighbouring cells.
        for j in range(n):
            hj = h[j]
            uj = u[j]
            for i in range(n - 1):
                hedge = 0.5 * (hj[i] + hj[i + 1])
                flux = uj[i] * dt / dx * hedge
                if flux > 0.0:
                    flux = min(flux, 0.4 * hj[i])
                elif flux < 0.0:
                    flux = max(flux, -0.4 * hj[i + 1])
                hj[i] -= flux
                hj[i + 1] += flux

        for j in range(n - 1):
            lower = h[j]
            upper = h[j + 1]
            vj = v[j]
            for i in range(n):
                hedge = 0.5 * (lower[i] + upper[i])
                flux = vj[i] * dt / dx * hedge
                if flux > 0.0:
                    flux = min(flux, 0.4 * lower[i])
                elif flux < 0.0:
                    flux = max(flux, -0.4 * upper[i])
                lower[i] -= flux
                upper[i] += flux

        ke = 0.0
        for j in range(n):
            hj = h[j]
            uj = u[j]
            vj = v[j]
            for i in range(n):
                ke += 0.5 * hj[i] * (uj[i] * uj[i] + vj[i] * vj[i])
        self.dissipated += ke * (1.0 - damp * damp)


class HydrostaticWater:
    """Global diffusive water solver: mass conserving, momentum free.

    Each sweep relaxes the free surface between neighbouring cells. Every
    transfer is applied to both cells with opposite sign, so total water
    volume is conserved to floating-point precision by construction.
    """

    def __init__(self, terrain, depth, rate=0.24):
        self.terrain = terrain
        self.n = terrain.n
        self.depth = depth
        self.rate = rate
        self.transported = 0.0

    def volume(self, cell_area=1.0):
        return sum(map(sum, self.depth)) * cell_area

    def step(self, sweeps=2):
        n = self.n
        bed = self.terrain.heights
        h = self.depth
        rate = self.rate
        moved = 0.0
        for _ in range(sweeps):
            for j in range(n):
                row = h[j]
                brow = bed[j]
                for i in range(n - 1):
                    flow = rate * ((brow[i] + row[i]) - (brow[i + 1] + row[i + 1]))
                    if flow > 0.0:
                        flow = min(flow, 0.25 * row[i])
                    elif flow < 0.0:
                        flow = max(flow, -0.25 * row[i + 1])
                    else:
                        continue
                    row[i] -= flow
                    row[i + 1] += flow
                    moved += abs(flow)

            for j in range(n - 1):
                lower = h[j]
                upper = h[j + 1]
                brow = bed[j]
                brow2 = bed[j + 1]
                for i in range(n):
                    flow = rate * ((brow[i] + lower[i]) - (brow2[i] + upper[i]))
                    if flow > 0.0:
                        flow = min(flow, 0.25 * lower[i])
                    elif flow < 0.0:
                        flow = max(flow, -0.25 * upper[i])
                    else:
                        continue
                    lower[i] -= flow
                    upper[i] += flow
                    moved += abs(flow)
        self.transported = moved
        return moved


class ThermalField:
    """Lumped-heat-capacity temperature field with conservative exchange.

    Capacity (dimensionless thermal mass) is 1 for land and 4 for water, so
    water bodies swing less than bare ground. Energy is ``T * capacity``;
    every diffusion transfer moves that quantity between cells with opposite
    sign, so internal exchange cannot create or destroy energy.
    """

    LAND_CAPACITY = 1.0
    WATER_CAPACITY = 4.0
    DIFFUSION = 0.02
    SOLAR_RATE = 5.5e-4      # K/s at full illumination, land
    COOLING_RATE = 2.2e-5    # 1/s toward sky temperature
    SKY_C = 2.0

    def __init__(self, terrain, temperature=12.0):
        n = terrain.n
        self.terrain = terrain
        self.temp = [[float(temperature)] * n for _ in range(n)]
        self.capacity = [[self.LAND_CAPACITY] * n for _ in range(n)]
        self.injected = 0.0
        self.radiated = 0.0
        self.capacity_adjustment = 0.0

    def total_energy(self):
        total = 0.0
        for j, row in enumerate(self.temp):
            cap = self.capacity[j]
            for i, value in enumerate(row):
                total += value * cap[i]
        return total

    def mean(self):
        return sum(map(sum, self.temp)) / (self.terrain.n ** 2)

    def step(self, dt, light, water_depth=None):
        n = self.terrain.n
        temp = self.temp
        cap = self.capacity
        if water_depth is not None:
            # Lumped thermal mass changes when water covers or uncovers a cell.
            # The energy implied by that mass change is booked separately so
            # the ledger still closes instead of hiding it inside the residual.
            for j in range(n):
                rowc = cap[j]
                roww = water_depth[j]
                rowt = temp[j]
                for i in range(n):
                    new_cap = (
                        self.WATER_CAPACITY if roww[i] > 0.05 else self.LAND_CAPACITY
                    )
                    old_cap = rowc[i]
                    if new_cap != old_cap:
                        self.capacity_adjustment += (new_cap - old_cap) * rowt[i]
                        rowc[i] = new_cap

        gain = self.SOLAR_RATE * clamp(light, 0.0, 1.0) * dt
        if gain:
            for j in range(n):
                capr = cap[j]
                row = temp[j]
                for i in range(n):
                    row[i] += gain
                    self.injected += gain * capr[i]

        cooling = self.COOLING_RATE * dt
        if cooling:
            for j in range(n):
                capr = cap[j]
                row = temp[j]
                for i in range(n):
                    delta = -cooling * (row[i] - self.SKY_C)
                    row[i] += delta
                    self.radiated -= delta * capr[i]

        k = self.DIFFUSION
        for j in range(n):
            row = temp[j]
            caprow = cap[j]
            for i in range(n - 1):
                ca = caprow[i]
                cb = caprow[i + 1]
                flow = k * (row[i] - row[i + 1]) * min(ca, cb)
                row[i] -= flow / ca
                row[i + 1] += flow / cb
        for j in range(n - 1):
            lower = temp[j]
            upper = temp[j + 1]
            ca_row = cap[j]
            cb_row = cap[j + 1]
            for i in range(n):
                ca = ca_row[i]
                cb = cb_row[i]
                flow = k * (lower[i] - upper[i]) * min(ca, cb)
                lower[i] -= flow / ca
                upper[i] += flow / cb

    def bounds(self):
        flat = [v for row in self.temp for v in row]
        return min(flat), max(flat)


class Plants:
    """Vegetation biomass on the terrain grid.

    Growth is limited by light, soil water availability and temperature, and
    saturates at a per-cell capacity. Biomass is a real consumable: agents
    remove it when they eat, and it regrows only where conditions allow.
    """

    GROWTH_RATE = 3.2e-5    # biomass/s at full factors

    def __init__(self, terrain, rng, seed_fraction=0.35):
        n = terrain.n
        self.terrain = terrain
        self.n = n
        self.biomass = [[0.0] * n for _ in range(n)]
        self.capacity = [[0.0] * n for _ in range(n)]
        for j in range(n):
            for i in range(n):
                x, y = terrain.cell_centre(i, j)
                slope = terrain.slope_magnitude(x, y)
                capacity = clamp(1.15 - 0.85 * slope, 0.0, 1.15)
                if terrain.heights[j][i] < 2.0:
                    capacity = 0.0
                self.capacity[j][i] = capacity
                if capacity > 0.2 and rng.random() < seed_fraction:
                    self.biomass[j][i] = capacity * rng.uniform(0.1, 0.8)

    def total(self):
        return sum(map(sum, self.biomass))

    def step(self, dt, light, temperature, water_depth):
        rate = self.GROWTH_RATE * dt
        if rate <= 0.0:
            return
        temp_factor = math.exp(-((temperature - 20.0) / 13.0) ** 2)
        if temp_factor <= 0.01:
            return
        n = self.n
        for j in range(n):
            row = self.biomass[j]
            capr = self.capacity[j]
            wetr = water_depth[j]
            for i in range(n):
                cap = capr[i]
                if cap <= 0.0:
                    continue
                b = row[i]
                if b >= cap:
                    continue
                moisture = 1.0 if wetr[i] > 0.02 else 0.3
                row[i] = b + rate * light * moisture * temp_factor * (cap - b) / cap

    def at_cell(self, i, j):
        return self.biomass[int(clamp(j, 0, self.n - 1))][int(clamp(i, 0, self.n - 1))]

    def harvest(self, i, j, amount):
        i = int(clamp(i, 0, self.n - 1))
        j = int(clamp(j, 0, self.n - 1))
        taken = min(amount, self.biomass[j][i])
        self.biomass[j][i] -= taken
        return taken
