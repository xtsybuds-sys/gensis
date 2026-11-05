"""Physiological inhabitant: body, drives, action execution, memory handle.

Rates are written per day of world time so the tuning is readable; the world
runs at whatever tick size the config selects.
"""

from __future__ import annotations

import math

from .sensors import INPUT_DIM
from .util import TAU, clamp

ENERGY_DRAIN_PER_DAY = 0.30
HYDRATION_DRAIN_PER_DAY = 1.10
NUTRITION_DRAIN_PER_DAY = 0.85
SLEEP_ENERGY_GAIN_PER_DAY = 0.55
DEHYDRATE_HEALTH_LOSS_PER_DAY = 0.95
STARVE_HEALTH_LOSS_PER_DAY = 0.55
RECOVERY_PER_DAY = 0.18

WALK_SPEED = 1.25          # m/s
TURN_RATE = 0.12           # rad/s
WALK_ENERGY_PER_M = 4.5e-4
MAX_WADE_DEPTH = 1.2       # no swimming yet: documented limitation
MAX_SLOPE = 1.0

DRINK_PER_MIN = 0.55       # hydration units per minute of drinking
EAT_PER_MIN = 0.40         # nutrition units per minute of eating
HARVEST_PER_MIN = 0.22     # biomass removed per minute of eating


class Inhabitant:
    def __init__(self, aid, name, brain, pos, heading=0.0, home_cell=(0, 0)):
        self.aid = aid
        self.name = name
        self.brain = brain
        self.pos = [float(pos[0]), float(pos[1])]
        self.home_cell = tuple(home_cell)
        self.heading = float(heading) % TAU
        self.alive = True
        self.born_tick = 0
        self.died_tick = None

        self.energy = 1.0
        self.hydration = 1.0
        self.nutrition = 0.85
        self.health = 1.0
        self.body_temp = 36.8
        self.age_s = 0.0
        self.sleeping = False
        self.just_woke = False

        self.distance_m = 0.0
        self.blocked_ticks = 0
        self.drinks = 0
        self.meals = 0
        self.sleep_seconds = 0.0

        self.last_actions = [0.0] * 6
        self.sensors = [0.0] * INPUT_DIM
        self.frame = {}
        self.pending = None

    # -- state of being ---------------------------------------------------
    @property
    def wellbeing(self):
        return (
            0.30 * self.energy
            + 0.28 * self.hydration
            + 0.22 * self.nutrition
            + 0.20 * self.health
        )

    def update(self, dt, world, actions, tick=0):
        """Advance physiology by ``dt`` seconds and apply the action vector."""
        events = {}
        if not self.alive:
            return events

        days = dt / 86400.0
        self.age_s += dt
        self.energy = clamp(self.energy - ENERGY_DRAIN_PER_DAY * days, 0.0, 1.0)
        self.hydration = clamp(
            self.hydration - HYDRATION_DRAIN_PER_DAY * days, 0.0, 1.0
        )
        self.nutrition = clamp(
            self.nutrition - NUTRITION_DRAIN_PER_DAY * days, 0.0, 1.0
        )

        ambient = world.temperature_at(self.pos[0], self.pos[1])
        target = 36.8 + 0.03 * (ambient - 18.0)
        self.body_temp += (target - self.body_temp) * min(1.0, 0.02 * dt)

        self.just_woke = False
        rest = clamp(actions[4], -1.0, 1.0)
        if rest > 0.45 and self.energy < 0.98:
            self.sleeping = True
        elif self.sleeping and (self.energy >= 0.98 or self.hydration < 0.15):
            self.sleeping = False
            self.just_woke = True
            events["woke"] = True

        if self.sleeping:
            self.energy = clamp(
                self.energy + SLEEP_ENERGY_GAIN_PER_DAY * days, 0.0, 1.0
            )
            self.sleep_seconds += dt
        else:
            self._move(dt, world, actions, events)
            self._consume(dt, world, actions, events)

        loss = 0.0
        if self.hydration <= 0.02:
            loss += DEHYDRATE_HEALTH_LOSS_PER_DAY
        if self.nutrition <= 0.02:
            loss += STARVE_HEALTH_LOSS_PER_DAY
        if self.body_temp < 33.0:
            loss += 0.4
        if loss:
            self.health = clamp(self.health - loss * days, 0.0, 1.0)
        elif self.health > 0.0 and self.hydration > 0.25 and self.nutrition > 0.25 \
                and not self.sleeping:
            self.health = clamp(self.health + RECOVERY_PER_DAY * days, 0.0, 1.0)

        if self.health <= 0.0:
            self.alive = False
            self.died_tick = tick
            events["died"] = True
        return events

    def _move(self, dt, world, actions, events):
        forward = clamp(actions[0], -1.0, 1.0)
        turn = clamp(actions[1], -1.0, 1.0)
        self.heading = (self.heading + turn * TURN_RATE * dt) % TAU
        if abs(forward) < 0.05:
            return
        distance = WALK_SPEED * min(1.0, abs(forward)) * dt
        if forward < 0.0:
            distance *= 0.4
        px, py = self.pos
        nx = px + math.cos(self.heading) * distance
        ny = py + math.sin(self.heading) * distance
        limit = world.cfg.world_size_m
        nx = clamp(nx, 1.0, limit - 1.0)
        ny = clamp(ny, 1.0, limit - 1.0)
        if world.water_depth_at(nx, ny) > MAX_WADE_DEPTH:
            self.blocked_ticks += 1
            events["blocked"] = "deep_water"
            return
        if world.terrain.slope_magnitude(nx, ny) > MAX_SLOPE:
            self.blocked_ticks += 1
            events["blocked"] = "steep_ground"
            return
        moved = math.hypot(nx - px, ny - py)
        self.pos = [nx, ny]
        self.distance_m += moved
        self.energy = clamp(self.energy - WALK_ENERGY_PER_M * moved, 0.0, 1.0)

    def _consume(self, dt, world, actions, events):
        minutes = dt / 60.0
        if actions[2] > 0.35 and world.water_depth_at(self.pos[0], self.pos[1]) > 0.08:
            self.hydration = clamp(self.hydration + DRINK_PER_MIN * minutes, 0.0, 1.0)
            self.drinks += 1
            events["drank"] = world.terrain.cell_of(self.pos[0], self.pos[1])
        if actions[3] > 0.35:
            ix, iy = world.terrain.cell_of(self.pos[0], self.pos[1])
            taken = world.plants.harvest(ix, iy, HARVEST_PER_MIN * minutes)
            if taken > 0.0:
                self.nutrition = clamp(self.nutrition + taken * 1.8, 0.0, 1.0)
                self.meals += 1
                events["ate"] = (ix, iy)

    # -- introspection ----------------------------------------------------
    def stats(self):
        return {
            "id": self.aid,
            "name": self.name,
            "alive": self.alive,
            "brain": self.brain.stats(),
            "pos": [round(self.pos[0], 1), round(self.pos[1], 1)],
            "heading": round(self.heading, 3),
            "energy": round(self.energy, 3),
            "hydration": round(self.hydration, 3),
            "nutrition": round(self.nutrition, 3),
            "health": round(self.health, 3),
            "body_temp": round(self.body_temp, 2),
            "sleeping": self.sleeping,
            "age_days": round(self.age_s / 86400.0, 3),
            "distance_m": round(self.distance_m, 1),
            "drinks": self.drinks,
            "meals": self.meals,
            "sleep_hours": round(self.sleep_seconds / 3600.0, 2),
            "blocked_ticks": self.blocked_ticks,
            "home_cell": list(self.home_cell),
            "died_tick": self.died_tick,
        }

    # -- persistence ------------------------------------------------------
    def state(self):
        return {
            "aid": self.aid,
            "name": self.name,
            "pos": self.pos,
            "home_cell": list(self.home_cell),
            "heading": self.heading,
            "alive": self.alive,
            "born_tick": self.born_tick,
            "died_tick": self.died_tick,
            "energy": self.energy,
            "hydration": self.hydration,
            "nutrition": self.nutrition,
            "health": self.health,
            "body_temp": self.body_temp,
            "age_s": self.age_s,
            "sleeping": self.sleeping,
            "distance_m": self.distance_m,
            "blocked_ticks": self.blocked_ticks,
            "drinks": self.drinks,
            "meals": self.meals,
            "sleep_seconds": self.sleep_seconds,
            "last_actions": self.last_actions,
            "sensors": self.sensors,
            "frame": self.frame,
            "pending": self.pending,
            "brain": self.brain.state_dict(),
        }

    def load(self, data):
        self.name = data["name"]
        self.pos = data["pos"]
        self.home_cell = tuple(data["home_cell"])
        self.heading = data["heading"]
        self.alive = data["alive"]
        self.born_tick = data["born_tick"]
        self.died_tick = data["died_tick"]
        self.energy = data["energy"]
        self.hydration = data["hydration"]
        self.nutrition = data["nutrition"]
        self.health = data["health"]
        self.body_temp = data["body_temp"]
        self.age_s = data["age_s"]
        self.sleeping = data["sleeping"]
        self.distance_m = data["distance_m"]
        self.blocked_ticks = data["blocked_ticks"]
        self.drinks = data["drinks"]
        self.meals = data["meals"]
        self.sleep_seconds = data["sleep_seconds"]
        self.last_actions = data["last_actions"]
        self.sensors = data["sensors"]
        self.frame = data.get("frame", {})
        self.pending = data.get("pending")
        self.brain.load(data["brain"])
