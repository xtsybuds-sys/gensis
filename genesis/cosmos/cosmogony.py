"""Reduced cosmogony: an expanding cloud collapses into a star and a disk of planets.

A reduced model, not a cosmological simulation. The rules, stated plainly:

- Gravity and angular momentum: each shell falls under the mass interior to it and is
  held up by its own angular momentum, a = -G M(<r)/r^2 + j^2/r^3. That centrifugal
  barrier turns infall into a disk instead of a point.
- Mass profile: M(<r) proportional to r, an isothermal-like cloud, so the inner shells
  carry enough mass to ignite a star.
- Conservation: shell mass, water and angular momentum survive mergers; the star grows
  only by accretion.
- Star: shells whose centrifugal radius is inside the star feed it; it ignites at
  IGNITION_MASS and its luminosity L ~ M^3.5 sets the habitable zone at
  0.95-1.37 sqrt(L).
- Disk: a falling shell stops where its angular momentum supports it,
  r = j^2 / (G M_star) - angular momentum conservation, not a chosen radius.
- Planets: settled shells within MERGE_WIDTH merge into one body (mass-weighted radius,
  summed water). A body only exists once it has settled; during infall there are none.
- Life: the water-rich body that ends inside the final habitable zone is the candidate.
  Its focus time is the first sample at which it is inside the zone at that time.

Times and G are scaled so the sequence is watchable. The outcome is not scripted: a
different cloud can fail to produce a habitable planet.
"""

from __future__ import annotations

import math
import random

G = 6.0
TOTAL_MASS = 1.0
SHELLS = 84
R_MAX = 1.0
H0 = 2.2             # initial expansion, visible before gravity turns it around
OMEGA = 1.55         # initial rotation, sets the disk
STAR_RADIUS = 0.045
IGNITION_MASS = 0.35
MERGE_WIDTH = 0.03
SNOW_LINE = 0.52
T_END = 2.0
DT = 0.001
SAMPLE = 0.02
WATER_MIN = 0.10


class Shell:
    __slots__ = ("r0", "mass", "water", "j", "angle", "samples", "accreted_at",
                 "settled_at")

    def __init__(self, r0, mass, water, j, angle):
        self.r0 = r0
        self.mass = mass
        self.water = water
        self.j = j
        self.angle = angle
        self.samples = []
        self.accreted_at = None
        self.settled_at = None


class Cosmogony:
    def __init__(self, seed=20261105):
        self.seed = seed
        rng = random.Random(seed)
        self.shells = []
        for i in range(SHELLS):
            r0 = R_MAX * (i + 0.5) / SHELLS
            mass = TOTAL_MASS / SHELLS
            jitter = 0.9 + 0.2 * rng.random()
            water = mass * (0.62 if r0 > SNOW_LINE else 0.03) * jitter
            self.shells.append(
                Shell(r0, mass, water, OMEGA * r0 * r0, rng.uniform(0.0, math.tau))
            )
        self.times = []
        self.star_mass_t = []
        self.hz_t = []
        self.planets_t = []
        self._integrate()
        self.star_mass = self.star_mass_t[-1]
        self.hz = self.hz_t[-1]
        self.planets = self.planets_t[-1]
        self.focus = None
        self.focus_tau = None
        candidates = [
            planet for planet in self.planets
            if self.hz[0] <= planet["radius"] <= self.hz[1]
            and planet["water_fraction"] >= WATER_MIN
        ]
        if candidates:
            self.focus = max(candidates, key=lambda planet: planet["water_fraction"])
            for index, planets in enumerate(self.planets_t):
                for planet in planets:
                    if abs(planet["radius"] - self.focus["radius"]) <= 0.02 \
                            and self.hz_t[index][0] <= planet["radius"] <= self.hz_t[index][1]:
                        self.focus_tau = self.times[index] / T_END
                        break
                if self.focus_tau is not None:
                    break

    # ------------------------------------------------------------------ physics
    def _enclosed(self, r0):
        return TOTAL_MASS * min(1.0, r0 / R_MAX)

    def _integrate(self):
        radius = [shell.r0 for shell in self.shells]
        vr = [H0 * shell.r0 for shell in self.shells]
        settled = [False] * SHELLS
        star_mass = 0.0
        steps = int(T_END / DT)
        sample_every = int(SAMPLE / DT)
        for step in range(steps + 1):
            if step % sample_every == 0:
                index = len(self.times)
                self.times.append(step * DT)
                self.star_mass_t.append(star_mass)
                luminosity = max(star_mass, 1e-6) ** 3.5
                self.hz_t.append((0.95 * math.sqrt(luminosity),
                                  1.37 * math.sqrt(luminosity)))
                for shell_index, shell in enumerate(self.shells):
                    shell.samples.append(radius[shell_index])
                self.planets_t.append(self._cluster(index))
            for index, shell in enumerate(self.shells):
                if shell.accreted_at is not None or settled[index]:
                    continue
                r = max(radius[index], STAR_RADIUS * 0.4)
                accel = -G * self._enclosed(shell.r0) / (r * r) + (shell.j * shell.j) / (r ** 3)
                vr[index] += accel * DT
                radius[index] += vr[index] * DT
                if radius[index] <= STAR_RADIUS:
                    radius[index] = STAR_RADIUS
                    shell.accreted_at = step * DT
                    star_mass += shell.mass
                    continue
                if star_mass > 0.05:
                    # Centrifugal barrier: the shell stops where its angular momentum
                    # supports it, or feeds the star if that radius is inside it.
                    r_c = (shell.j * shell.j) / (G * star_mass)
                    if r_c <= STAR_RADIUS:
                        radius[index] = STAR_RADIUS
                        shell.accreted_at = step * DT
                        star_mass += shell.mass
                        continue
                    if radius[index] <= r_c and vr[index] < 0.0:
                        radius[index] = r_c
                        vr[index] = 0.0
                        settled[index] = True
                        shell.settled_at = step * DT
        self.star_mass = star_mass

    def _cluster(self, index):
        now = self.times[index]
        bodies = []
        for shell in self.shells:
            if shell.settled_at is None or shell.settled_at > now:
                continue
            if shell.accreted_at is not None and shell.accreted_at <= now:
                continue
            r = shell.samples[index]
            if r <= STAR_RADIUS * 1.001:
                continue
            bodies.append((r, shell))
        bodies.sort(key=lambda item: item[0])
        clusters = []
        for r, shell in bodies:
            if clusters and abs(r - clusters[-1]["radius"]) <= MERGE_WIDTH:
                cluster = clusters[-1]
                total = cluster["mass"] + shell.mass
                cluster["radius"] = (
                    cluster["radius"] * cluster["mass"] + r * shell.mass
                ) / total
                cluster["mass"] = total
                cluster["water"] += shell.water
                cluster["angle"] = shell.angle
            else:
                clusters.append({
                    "radius": r,
                    "mass": shell.mass,
                    "water": shell.water,
                    "angle": shell.angle,
                })
        minimum = TOTAL_MASS / SHELLS * 2.0
        out = []
        for cluster in clusters:
            if cluster["mass"] < minimum:
                continue
            out.append({
                "radius": cluster["radius"],
                "mass": cluster["mass"],
                "water": cluster["water"],
                "water_fraction": cluster["water"] / max(cluster["mass"], 1e-9),
                "angle": cluster["angle"],
            })
        return out

    # ------------------------------------------------------------------ playback
    def _index(self, tau):
        tau = max(0.0, min(0.999999, tau))
        position = tau * (len(self.times) - 1)
        low = int(position)
        high = min(low + 1, len(self.times) - 1)
        return low, high, position - low

    def phase(self, tau):
        if tau < 0.16:
            return "expansion"
        if tau < 0.38:
            return "collapse"
        index = min(int(tau * (len(self.times) - 1)), len(self.times) - 1)
        if self.star_mass_t[index] < IGNITION_MASS:
            return "ignition"
        if tau < 0.66:
            return "disk"
        if self.focus is not None and self.focus_tau is not None and tau >= self.focus_tau:
            return "life"
        return "planets"

    def frame(self, tau=None):
        tau = 0.0 if tau is None else max(0.0, min(0.999999, tau))
        low, high, blend = self._index(tau)
        star_mass = self.star_mass_t[low] * (1.0 - blend) + self.star_mass_t[high] * blend
        planets_src = self.planets_t[high] if blend > 0.5 else self.planets_t[low]
        t = self.times[low] * (1.0 - blend) + self.times[high] * blend
        points = []
        for index, shell in enumerate(self.shells):
            r = shell.samples[low] * (1.0 - blend) + shell.samples[high] * blend
            if r <= STAR_RADIUS * 1.01:
                continue
            water_fraction = shell.water / max(shell.mass, 1e-9)
            spread = 1.0 if t < 0.7 else 0.035
            for k in range(6):
                angle = shell.angle + k * (math.tau / 6.0) + t * 0.6
                lift = (index % 9 - 4) * 0.03
                x = r * math.cos(angle) * spread
                z = r * math.sin(angle) * spread
                y = r * math.sin(lift) * (0.55 if t < 0.7 else 0.04)
                points.append([
                    round(x, 4), round(y, 4), round(z, 4),
                    round(0.006 + water_fraction * 0.02, 4),
                    1 if water_fraction > 0.2 else 0,
                ])
        planets = []
        for planet in planets_src:
            planets.append({
                "radius": round(planet["radius"], 4),
                "mass": round(planet["mass"], 5),
                "water": round(planet["water_fraction"], 3),
                "angle": round((planet["angle"] + t * 1.1) % math.tau, 4),
                "in_hz": self.hz_t[low][0] <= planet["radius"] <= self.hz_t[low][1],
                "focus": bool(self.focus is not None
                              and abs(planet["radius"] - self.focus["radius"]) < 1e-3),
            })
        return {
            "tau": round(tau, 4),
            "phase": self.phase(tau),
            "model_time": round(t, 4),
            "star_mass": round(star_mass, 4),
            "star_ignited": star_mass >= IGNITION_MASS,
            "star_radius": round(0.012 + 0.05 * min(1.0, star_mass / 0.6), 4),
            "hz": [round(self.hz_t[low][0], 4), round(self.hz_t[low][1], 4)],
            "planets": planets,
            "focus": None if self.focus is None else {
                "radius": round(self.focus["radius"], 4),
                "mass": round(self.focus["mass"], 5),
                "water": round(self.focus["water_fraction"], 3),
            },
            "points": points,
        }

    def summary(self):
        return {
            "star_mass": round(self.star_mass, 4),
            "hz": [round(self.hz[0], 4), round(self.hz[1], 4)],
            "planets": [
                {
                    "radius": round(p["radius"], 4),
                    "mass": round(p["mass"], 5),
                    "water": round(p["water_fraction"], 3),
                }
                for p in self.planets
            ],
            "focus": None if self.focus is None else {
                "radius": round(self.focus["radius"], 4),
                "water": round(self.focus["water_fraction"], 3),
            },
            "focus_tau": None if self.focus_tau is None else round(self.focus_tau, 3),
        }
