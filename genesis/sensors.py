"""Sensory model: raycast vision, local field sampling, proprioception.

An inhabitant receives exactly one fixed-width vector per observation, and
every element is produced by sampling the simulation from the agent's own
position. There is no channel that exposes global world state, which is the
information firewall described in the specification.

The last four elements were added for the calibration sprint (Muse's decision 4a):
a conspecific channel (nearest peer proximity, plus its bearing relative to the
inhabitant's own heading as cosine/sine) and the inhabitant's own social drive
(isolation level). Before this, no inhabitant could perceive another at all, so
no social behaviour could ever be observed - measured closest approach over five
days at 1024 m was 342.8 m with a 40 m sense range.

Range is 15 m (Muse decision 2, 2026-11-05): at 40 m the five houses at 128 m all
started inside the peer range, so `first_sighting_day` was a constant 0.0 and
"starts unaware" was false. 15 m keeps reproduction reachable while making first
contact an event rather than a spawn condition.

Limitation, deliberate and logged: peer detection is proximity-based inside
``CONSPECIFIC_RANGE_M`` with no terrain-occlusion test. A single nearest peer is
reported rather than all peers, because the vector width is part of the
architecture and widening it again is a decision, not an implementation detail.
"""

from __future__ import annotations

import math

from .util import TAU, clamp

INPUT_DIM = 28
RAY_COUNT = 8
RAY_RANGE_M = 40.0
RAY_STEPS = 16
EYE_HEIGHT_M = 1.7
CONSPECIFIC_RANGE_M = 15.0

CODE_NONE = 0.0
CODE_WATER = 0.33
CODE_PLANT = 0.66
CODE_ROCK = 1.0

# Index map for the appended social channels (the 24-dim layout is unchanged).
PEER_PROXIMITY_INDEX = 24
PEER_BEARING_COS_INDEX = 25
PEER_BEARING_SIN_INDEX = 26
ISOLATION_INDEX = 27


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


def nearest_peer(agent, agents, max_range=CONSPECIFIC_RANGE_M):
    """Nearest living conspecific: (proximity, relative_bearing, distance_m).

    Relative bearing is measured from the agent's own heading in [-pi, pi], so
    the inhabitant has to integrate its own orientation to use it - the channel
    is egocentric, not a world-frame map.
    """
    best = None
    x0, y0 = agent.pos
    for other in agents or ():
        if other is agent or not other.alive:
            continue
        dx = other.pos[0] - x0
        dy = other.pos[1] - y0
        distance = math.hypot(dx, dy)
        if distance > max_range:
            continue
        if best is not None and distance >= best[2]:
            continue
        angle = math.atan2(dy, dx) - agent.heading
        bearing = (angle + math.pi) % TAU - math.pi
        best = (1.0 - distance / max_range, bearing, distance)
    return best


def sense(agent, world, agents=None):
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

    peer = nearest_peer(agent, agents)
    if peer is None:
        peer_proximity, peer_cos, peer_sin, peer_distance = 0.0, 0.0, 0.0, None
    else:
        peer_proximity, bearing, peer_distance = peer
        peer_cos = math.cos(bearing) if peer_distance else 0.0
        peer_sin = math.sin(bearing) if peer_distance else 0.0
    isolation = clamp(getattr(agent, "isolation", 0.0), 0.0, 1.0)

    vector = (
        proximities
        + codes
        + [light, slope, thirst, hunger, fatigue, warmth, health, day]
        + [peer_proximity, peer_cos, peer_sin, isolation]
    )
    frame = {
        "proximity": proximities,
        "codes": codes,
        "distance_m": [round(d, 1) for d in distances],
        "light": round(light, 3),
        "conspecific": {
            "proximity": round(peer_proximity, 3),
            "bearing": round(math.atan2(peer_sin, peer_cos), 3) if peer_proximity else None,
            "distance_m": None if peer_distance is None else round(peer_distance, 1),
        },
    }
    return vector, frame
