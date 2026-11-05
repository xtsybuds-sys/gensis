"""A bounded 2D dish with three nutrient patches.

The dish is the pilot's whole environment: no light gradient beyond a static cue, no
toxins, no predators. Nutrient is consumed by cells, diffuses between cells, and
regrows toward a cap inside the three patches, so the dish can be depleted and can
recover. Nothing enters or leaves at the walls.
"""

from __future__ import annotations

import math

from ..util import clamp

PATCH_CENTRES = ((4.0, 4.0), (12.0, 4.0), (8.0, 12.0))
PATCH_RADIUS_M = 3.0
PATCH_ID = (-1, -1, -1)


class NutrientDish:
    def __init__(self, size_m=16.0, grid=64, cap=1.0, regrow=0.004,
                 diffusion=0.02, initial=0.9):
        self.size_m = float(size_m)
        self.grid = int(grid)
        self.cell_m = self.size_m / self.grid
        self.cap = float(cap)
        self.regrow = float(regrow)
        self.diffusion = float(diffusion)
        self.values = [0.0] * (self.grid * self.grid)
        self.patch_mask = [-1] * (self.grid * self.grid)
        for j in range(self.grid):
            for i in range(self.grid):
                x, y = self.centre(i, j)
                for patch, (px, py) in enumerate(PATCH_CENTRES):
                    if math.hypot(x - px, y - py) <= PATCH_RADIUS_M:
                        idx = j * self.grid + i
                        self.patch_mask[idx] = patch
                        self.values[idx] = initial
                        break

    def centre(self, i, j):
        return (i + 0.5) * self.cell_m, (j + 0.5) * self.cell_m

    def _index(self, x, y):
        i = int(clamp(x / self.cell_m, 0, self.grid - 1))
        j = int(clamp(y / self.cell_m, 0, self.grid - 1))
        return j * self.grid + i

    def at(self, x, y):
        return self.values[self._index(x, y)]

    def patch_at(self, x, y):
        return self.patch_mask[self._index(x, y)]

    def take(self, x, y, amount):
        idx = self._index(x, y)
        have = self.values[idx]
        got = have if have < amount else amount
        self.values[idx] = have - got
        return got

    def gradient(self, x, y):
        step = self.cell_m
        gx = (self.at(x + step, y) - self.at(x - step, y)) / (2.0 * step)
        gy = (self.at(x, y + step) - self.at(x, y - step)) / (2.0 * step)
        return gx, gy

    def step(self):
        """One slow-field update: conservative diffusion, then capped regrowth."""
        grid = self.grid
        old = self.values
        new = list(old)
        k = self.diffusion
        # No-flux walls: an out-of-range neighbour reflects the cell's own value, so
        # the exchange stays symmetric and the nutrient ledger is conserved exactly.
        for j in range(grid):
            row = j * grid
            for i in range(grid):
                idx = row + i
                v = old[idx]
                left = old[idx - 1] if i > 0 else v
                right = old[idx + 1] if i < grid - 1 else v
                up = old[idx - grid] if j > 0 else v
                down = old[idx + grid] if j < grid - 1 else v
                neighbours = (left + right + up + down) * 0.25
                new[idx] = v + k * (neighbours - v)
        mask = self.patch_mask
        cap = self.cap
        regrow = self.regrow
        for idx, patch in enumerate(mask):
            if patch >= 0:
                value = new[idx] + regrow
                new[idx] = cap if value > cap else value
        self.values = new

    def total(self):
        return sum(self.values)
