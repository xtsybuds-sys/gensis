"""Sensory model: raycast vision, local field sampling, proprioception.

An inhabitant receives exactly one fixed-width vector per observation, and
every element is produced by sampling the simulation from the agent's own
position. There is no channel that exposes global world state, which is the
information firewall described in the specification.
"""

from __future__ import annotations

import math

from .util import TAU, clamp

INPUT_DIM = 24
RAY_COUNT = 8
RAY_RANGE_M = 40.0
RAY_STEPS = 16
EYE_HEIGHT_M = 1.7

CODE_NONE = 0.0
CODE_WATER = 0.33
CODE_PLANT = 0.66
CODE_ROCK = 1.0


def surface_code(world, x, y):
    if world.water_depth_at(x, y) > 0.15:
        return CODE_WATER
    if world.biomass_at(x, y) > 0.12:
        return CODE_PLANT
    if world.terrain.slope_magnitude(x, y) > 0.75:
        return CODE_ROCK
    return CODE_NONE


def cast_ray(world, x0, y0, angle, max_range=RAY_RANGE_M, steps=RAY_STEPS):
    """March one ray. Returns (proximity, surface_code, distance_m)."""
    eye_z = world.terrain.sample(x0, y0) + EYE_HEIGHT_M
    dx = math.cos(angle)
    dy = math.sin(angle)
    step = max_range / steps
    limit = world.cfg.world_size_m
    code = CODE_NONE
    for s in range(1, steps + 1):
        d = s * step
        x = x0 + dx * d
        y = y0 + dy * d
        if x < 0.0 or y < 0.0 or x > limit or y > limit:
            return 1.0 - d / max_range, code or CODE_ROCK, d
        if world.terrain.sample(x, y) > eye_z:
            return 1.0 - d / max_range, code or CODE_ROCK, d
        if code == CODE_NONE:
            code = surface_code(world, x, y)
    return 0.0, code, max_range


def sense(agent, world):
    """Build the sensor vector plus a display frame for the observer UI."""
    x0, y0 = agent.pos
    proximities = []
    codes = []
    distances = []
    for r in range(RAY_COUNT):
        angle = agent.heading + r * (TAU / RAY_COUNT)
        proximity, code, distance = cast_ray(world, x0, y0, angle)
        proximities.append(proximity)
        codes.append(code)
        distances.append(distance)

    light = world.light()
    slope = clamp(world.terrain.slope_magnitude(x0, y0), 0.0, 1.5)
    thirst = clamp(1.0 - agent.hydration, 0.0, 1.0)
    hunger = clamp(1.0 - agent.nutrition, 0.0, 1.0)
    fatigue = clamp(1.0 - agent.energy, 0.0, 1.0)
    warmth = clamp((agent.body_temp - 30.0) / 12.0, 0.0, 1.0)
    health = clamp(agent.health, 0.0, 1.0)
    day = 0.5 + 0.5 * math.sin(TAU * world.day_phase())

    vector = (
        proximities
        + codes
        + [light, slope, thirst, hunger, fatigue, warmth, health, day]
    )
    frame = {
        "proximity": proximities,
        "codes": codes,
        "distance_m": [round(d, 1) for d in distances],
        "light": round(light, 3),
    }
    return vector, frame
