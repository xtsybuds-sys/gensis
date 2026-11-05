from __future__ import annotations

from ..util import clamp, lerp, smoothstep


class Terrain:
    """Regular-grid heightfield. ``heights[row=j][col=i]`` is in metres."""

    __slots__ = ("n", "size_m", "cell_m", "heights")

    def __init__(self, heights, size_m):
        self.heights = heights
        self.n = len(heights)
        self.size_m = float(size_m)
        self.cell_m = self.size_m / self.n

    def at_cell(self, i, j):
        n = self.n
        i = int(clamp(i, 0, n - 1))
        j = int(clamp(j, 0, n - 1))
        return self.heights[j][i]

    def sample(self, x, y):
        """Bilinear height lookup; coordinates in metres."""
        n = self.n
        gx = clamp(x / self.cell_m, 0.0, n - 1.000001)
        gy = clamp(y / self.cell_m, 0.0, n - 1.000001)
        i = int(gx)
        j = int(gy)
        tx = gx - i
        ty = gy - j
        h00 = self.heights[j][i]
        h10 = self.heights[j][i + 1]
        h01 = self.heights[j + 1][i]
        h11 = self.heights[j + 1][i + 1]
        return lerp(lerp(h00, h10, tx), lerp(h01, h11, tx), ty)

    def slope(self, x, y, eps=None):
        eps = eps if eps is not None else self.cell_m * 0.5
        dzdx = (self.sample(x + eps, y) - self.sample(x - eps, y)) / (2.0 * eps)
        dzdy = (self.sample(x, y + eps) - self.sample(x, y - eps)) / (2.0 * eps)
        return dzdx, dzdy

    def slope_magnitude(self, x, y):
        dzdx, dzdy = self.slope(x, y)
        return (dzdx * dzdx + dzdy * dzdy) ** 0.5

    def cell_of(self, x, y):
        return (
            int(clamp(x / self.cell_m, 0, self.n - 1)),
            int(clamp(y / self.cell_m, 0, self.n - 1)),
        )

    def cell_centre(self, i, j):
        return ((i + 0.5) * self.cell_m, (j + 0.5) * self.cell_m)

    def summary(self):
        flat = [h for row in self.heights for h in row]
        return {
            "cells": self.n * self.n,
            "cell_m": round(self.cell_m, 3),
            "min_m": round(min(flat), 3),
            "max_m": round(max(flat), 3),
            "mean_m": round(sum(flat) / len(flat), 3),
        }


def _lattice(rng, cells):
    return [[rng.random() for _ in range(cells + 1)] for _ in range(cells + 1)]


def _value_noise(lattice, u, v):
    f = len(lattice) - 1
    x = clamp(u, 0.0, 1.0) * f
    y = clamp(v, 0.0, 1.0) * f
    i = min(int(x), f - 1)
    j = min(int(y), f - 1)
    tx = smoothstep(x - i)
    ty = smoothstep(y - j)
    top = lerp(lattice[j][i], lattice[j][i + 1], tx)
    bottom = lerp(lattice[j + 1][i], lattice[j + 1][i + 1], tx)
    return lerp(top, bottom, ty)


def generate_terrain(n, size_m, rng, octaves=4, base=4, persistence=0.5,
                     lacunarity=2.0, relief_m=52.0):
    """Fractal value-noise terrain shaped to give ocean, coast and highlands."""
    lattices = []
    freq = float(base)
    amp = 1.0
    total = 0.0
    for _ in range(octaves):
        lattices.append((_lattice(rng, max(1, int(round(freq)))), amp))
        total += amp
        amp *= persistence
        freq *= lacunarity

    heights = [[1.0] * n for _ in range(n)]
    for j in range(n):
        v = j / (n - 1)
        row = heights[j]
        for i in range(n):
            u = i / (n - 1)
            acc = 0.0
            for lat, weight in lattices:
                acc += weight * _value_noise(lat, u, v)
            shaped = (acc / total) ** 1.9
            row[i] = 1.0 + relief_m * shaped
    return Terrain(heights, size_m)
