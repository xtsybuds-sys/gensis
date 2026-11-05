"""Validation suite: physics conservation, integrator accuracy, learning.

Every check returns a dict so the CLI and the test suite share one definition
of "validated". Each entry carries a numeric tolerance; none of these is a
smoke test.
"""

from __future__ import annotations

import math
import pickle
import random

from .agents import SLEEP_BOUT_MAX_S
from .brains import BRAIN_KINDS, make_brain
from .config import Config
from .physics import (
    BallisticSystem,
    HydrostaticWater,
    PhysicsWorld,
    ShallowWater,
    Sphere,
    Terrain,
    generate_terrain,
)
from .physics.fields import ThermalField
from .sensors import INPUT_DIM, RAY_RANGE_M, sense
from .sim import Simulation


def _check(name, passed, **detail):
    return {"check": name, "passed": bool(passed), "detail": detail}


def flat_terrain(n=8, size_m=80.0, height=0.0):
    return Terrain([[height] * n for _ in range(n)], size_m)


# -- physics ---------------------------------------------------------------
def check_water_mass_conservation():
    rng = random.Random(7)
    n = 12
    terrain = generate_terrain(n, 120.0, rng)
    depth = [
        [max(0.0, 8.0 - terrain.heights[j][i]) for i in range(n)] for j in range(n)
    ]
    field = HydrostaticWater(terrain, depth)
    start = field.volume(terrain.cell_m ** 2)
    for _ in range(60):
        field.step(sweeps=2)
    end = field.volume(terrain.cell_m ** 2)
    drift = abs(end - start)
    return _check(
        "physics/water-mass-conservation",
        drift <= 1e-6 * max(1.0, start),
        start_m3=round(start, 4),
        end_m3=round(end, 4),
        drift_m3=drift,
    )


def check_shallow_water_dynamics():
    n = 12
    terrain = flat_terrain(n, 120.0)
    depth = [[0.0] * n for _ in range(n)]
    for j in range(4, 8):
        for i in range(4, 8):
            depth[j][i] = 2.0
    field = ShallowWater(terrain, depth, friction=0.02)
    start = field.volume()
    peak_start = max(map(max, field.depth))
    for _ in range(300):
        field.step(field.dt_limit)
    end = field.volume()
    peak_end = max(map(max, field.depth))
    mass_ok = abs(end - start) <= 1e-9 * max(1.0, start)
    redistributed = peak_end < peak_start and field.depth[0][0] > 0.0
    return _check(
        "physics/shallow-water-mass-and-flow",
        mass_ok and redistributed,
        start_m3=round(start, 6),
        end_m3=round(end, 6),
        peak_start=round(peak_start, 4),
        peak_end=round(peak_end, 4),
        corner_depth=round(field.depth[0][0], 6),
    )


def check_thermal_diffusion_conservation():
    terrain = flat_terrain(10, 100.0)
    field = ThermalField(terrain, temperature=20.0)
    field.COOLING_RATE = 0.0
    field.temp[0][0] = 80.0
    start = field.total_energy()
    for _ in range(120):
        field.step(10.0, 0.0, None)
    end = field.total_energy()
    drift = abs(end - start)
    spread = field.temp[5][5] - 20.0
    return _check(
        "physics/thermal-diffusion-conservation",
        drift <= 1e-9 * max(1.0, abs(start)) and spread > 0.0,
        start_energy=round(start, 6),
        end_energy=round(end, 6),
        drift=drift,
        spread_to_centre_k=round(spread, 6),
    )


def check_thermal_ledger():
    cfg = Config(grid=10, population=0, days=0.2, checkpoint_every=0, log_every=0)
    rng = random.Random(11)
    world = PhysicsWorld(cfg, rng)
    for tick in range(1, 601):
        world.step(cfg.tick_seconds, tick)
    report = world.conservation()
    scale = max(
        1.0, abs(world.thermal.injected) + abs(world.thermal.radiated)
    )
    residual = report["thermal_residual"]
    return _check(
        "physics/thermal-energy-ledger",
        abs(residual) <= 0.02 * scale,
        residual=residual,
        scale=round(scale, 4),
        injected=round(world.thermal.injected, 4),
        radiated=round(world.thermal.radiated, 4),
        capacity_adjustment=round(world.thermal.capacity_adjustment, 4),
    )


def check_free_fall_accuracy():
    terrain = flat_terrain(8, 80.0)
    system = BallisticSystem(terrain)
    body = Sphere((40.0, 40.0, 100.0), (0.0, 0.0, 0.0), restitution=0.5, drag=0.0)
    system.add(body)
    dt = 0.01
    for _ in range(200):
        system.step(dt, substeps=1)
    expected = 100.0 - 0.5 * 9.81 * (200 * dt) ** 2
    error = abs(body.pos[2] - expected)
    return _check(
        "physics/free-fall-analytic",
        error < 1e-6 * max(1.0, abs(expected)),
        simulated_z=round(body.pos[2], 9),
        analytic_z=round(expected, 9),
        abs_error=error,
    )


def check_ballistic_energy_drift():
    terrain = flat_terrain(8, 80.0)
    system = BallisticSystem(terrain)
    body = Sphere((40.0, 40.0, 200.0), (3.0, 0.0, 0.0), restitution=0.0, drag=0.0)
    system.add(body)
    start = system.mechanical_energy()
    for _ in range(150):
        system.step(0.01, substeps=1)
    end = system.mechanical_energy()
    drift = abs(end - start) / max(1.0, abs(start))
    return _check(
        "physics/ballistic-energy-drift",
        drift < 1e-9,
        start_j=round(start, 6),
        end_j=round(end, 6),
        relative_drift=drift,
    )


def check_restitution():
    terrain = flat_terrain(8, 80.0)
    restitution = 0.6
    system = BallisticSystem(terrain)
    body = Sphere(
        (40.0, 40.0, 5.25),
        (0.0, 0.0, 0.0),
        radius=0.25,
        restitution=restitution,
        drag=0.0,
        friction=0.0,
    )
    system.add(body)
    apex = 0.0
    for _ in range(4000):
        system.step(0.005, substeps=1)
        if system.contacts:
            apex = max(apex, body.pos[2] - 0.25)
    expected = restitution ** 2 * 5.0
    error = abs(apex - expected) / expected
    return _check(
        "physics/restitution-apex",
        error < 0.12,
        apex_m=round(apex, 4),
        expected_m=round(expected, 4),
        relative_error=round(error, 5),
        dissipated_j=round(system.dissipated, 4),
    )


# -- integration -----------------------------------------------------------
def _small_cfg(**kw):
    base = dict(
        days=0.02,
        grid=12,
        population=3,
        checkpoint_every=0,
        log_every=0,
    )
    base.update(kw)
    return Config(**base)


def check_determinism():
    cfg = _small_cfg()
    a = Simulation(cfg)
    b = Simulation(cfg)
    for _ in range(60):
        a.step()
    for _ in range(60):
        b.step()
    return _check(
        "integration/determinism",
        a.digest() == b.digest(),
        seed=cfg.seed,
        digest_a=a.digest(),
        digest_b=b.digest(),
        ticks=a.tick,
    )


def check_checkpoint_resume():
    cfg = _small_cfg()
    a = Simulation(cfg)
    for _ in range(40):
        a.step()
    blob = pickle.dumps(a.state(), protocol=pickle.HIGHEST_PROTOCOL)
    b = Simulation(cfg)
    b.load_state(pickle.loads(blob))
    resumed_tick = b.tick
    for _ in range(40):
        a.step()
    for _ in range(40):
        b.step()
    return _check(
        "integration/checkpoint-resume-identity",
        a.digest() == b.digest() and a.tick == b.tick,
        checkpoint_tick=resumed_tick,
        checkpoint_bytes=len(blob),
        digest_a=a.digest(),
        digest_b=b.digest(),
    )


def check_population_setup():
    cfg = _small_cfg(population=5)
    sim = Simulation(cfg)
    cells = [a.home_cell for a in sim.agents]
    distinct = len(set(cells)) == 5
    on_land = all(
        sim.world.terrain.heights[c[1]][c[0]] > cfg.water_level_m for c in cells
    )
    centres = [sim.world.terrain.cell_centre(*c) for c in cells]
    separation = min(
        math.hypot(centres[i][0] - centres[j][0], centres[i][1] - centres[j][1])
        for i in range(len(centres))
        for j in range(i + 1, len(centres))
    )
    kinds = sorted({a.brain.kind for a in sim.agents})
    return _check(
        "integration/five-separate-houses",
        distinct
        and on_land
        and separation >= max(12.0, 0.10 * cfg.world_size_m)
        and kinds == ["hybrid", "neural"],
        houses=len(cells),
        distinct=distinct,
        min_separation_m=round(separation, 1),
        on_land=on_land,
        brain_kinds=kinds,
    )


# -- intelligence ----------------------------------------------------------
def check_prediction_learning():
    rng = random.Random(3)
    brain = make_brain("neural", rng, Config())
    x = [math.sin(i * 0.5) for i in range(INPUT_DIM)]
    early = []
    late = []
    for step in range(240):
        brain.act(x)
        target = x[1:] + [x[0]]
        brain.learn(0.0, target)
        if step < 20:
            early.append(brain.last_mse)
        if step >= 220:
            late.append(brain.last_mse)
        x = target
    start = sum(early) / len(early)
    end = sum(late) / len(late)
    return _check(
        "intelligence/forward-model-learning",
        end < 0.25 * start,
        early_mse=round(start, 6),
        late_mse=round(end, 6),
        reduction=round(1.0 - end / start, 4) if start else 0.0,
    )


def check_brain_parity():
    rng = random.Random(9)
    cfg = Config()
    x = [0.1] * INPUT_DIM
    shapes = []
    for kind in BRAIN_KINDS:
        brain = make_brain(kind, rng, cfg)
        out = brain.act(x)
        shapes.append((len(out), max(abs(v) for v in out) <= 1.0))
        brain.learn(0.1, x)
    return _check(
        "intelligence/architectures-comparable",
        [s[0] for s in shapes] == [6, 6] and all(s[1] for s in shapes),
        brain_kinds=list(BRAIN_KINDS),
        output_dims=[s[0] for s in shapes],
        bounded=all(s[1] for s in shapes),
        sensor_input_dim=INPUT_DIM,
    )


def check_sensory_firewall():
    cfg = Config(grid=16, population=1, days=0.01)
    sim = Simulation(cfg)
    agent = sim.agents[0]
    vector, frame = sense(agent, sim.world)
    length_ok = len(vector) == INPUT_DIM
    range_ok = max(frame["distance_m"]) <= RAY_RANGE_M + 1e-6
    ix, iy = sim.world.terrain.cell_of(agent.pos[0], agent.pos[1])
    cell = sim.world.terrain.cell_m
    # Farthest grid corner, whatever the world size: the check is that a change
    # beyond sense range cannot alter perception, not that the world is 1024 m.
    far_x, far_y = max(
        ((cx, cy) for cx in (0, cfg.grid - 1) for cy in (0, cfg.grid - 1)),
        key=lambda c: math.hypot((c[0] - ix) * cell, (c[1] - iy) * cell),
    )
    distance = math.hypot((far_x - ix) * cell, (far_y - iy) * cell)
    before = list(vector)
    sim.world.water.depth[far_y][far_x] = 9.0
    after, _ = sense(agent, sim.world)
    return _check(
        "intelligence/sensory-firewall",
        length_ok
        and range_ok
        and before == after
        and distance > RAY_RANGE_M * 1.5,
        sensor_dim=len(vector),
        max_ray_m=max(frame["distance_m"]),
        altered_cell_distance_m=round(distance, 1),
        perception_unchanged=before == after,
    )


def check_death_permanence():
    cfg = _small_cfg(population=1, grid=10)
    sim = Simulation(cfg)
    agent = sim.agents[0]
    agent.health = 0.0
    sim.step()
    died = (not agent.alive) and agent.died_tick is not None
    for _ in range(20):
        sim.step()
    still_dead = not agent.alive
    recorded = any(e["kind"] == "death" for e in sim.recent_events)
    return _check(
        "biology/permanent-death-recorded",
        died and still_dead and recorded,
        died=died,
        remains_dead=still_dead,
        death_event=recorded,
        died_tick=agent.died_tick,
    )


def check_knowledge_transfer():
    rng = random.Random(5)
    cfg = Config()
    sender = make_brain("hybrid", rng, cfg, "sender")
    receiver = make_brain("hybrid", rng, cfg, "receiver")
    sender.tokens.add("water:3,4")
    sender.remember_place(3, 4, "water")
    shared = sender.share_with(receiver)
    return _check(
        "social/knowledge-transfer",
        "water:3,4" in receiver.tokens
        and receiver.known_places.get("3,4") == "water"
        and bool(shared),
        shared=shared,
        receiver_tokens=len(receiver.tokens),
    )


def check_dawn_start():
    cfg = _small_cfg()
    sim = Simulation(cfg)
    clock = sim.world.clock()
    light = sim.world.light()
    return _check(
        "environment/lives-start-at-dawn",
        clock.startswith("day 1 06:") and light > 0.05,
        clock=clock,
        light=round(light, 3),
        start_hour=cfg.start_hour,
    )


def check_conspecific_channel():
    """An inhabitant can perceive a peer, egocentrically, and only when close."""
    cfg = _small_cfg(population=2)
    sim = Simulation(cfg)
    a, b = sim.agents[0], sim.agents[1]
    a.heading = 0.0
    b.pos = [a.pos[0], min(cfg.world_size_m - 2.0, a.pos[1] + 5.0)]
    vector, frame = sense(a, sim.world, sim.agents)
    proximity, cos_b, sin_b, isolation = vector[-4:]
    alone, _ = sense(a, sim.world, [a])
    return _check(
        "intelligence/conspecific-channel",
        len(vector) == INPUT_DIM
        and proximity > 0.5
        and sin_b > 0.9
        and abs(cos_b) < 0.1
        and alone[24] == 0.0
        and frame["conspecific"]["distance_m"] is not None,
        sensor_dim=len(vector),
        peer_proximity=round(proximity, 3),
        bearing_sin=round(sin_b, 3),
        bearing_cos=round(cos_b, 3),
        alone_peer_element=alone[24],
        isolation_element=round(isolation, 3),
    )


def check_social_drive():
    """Isolation rises alone and is relieved by a peer: a homeostatic drive."""
    cfg = _small_cfg(population=1)
    sim = Simulation(cfg)
    agent = sim.agents[0]
    agent.nearest_peer_m = None
    for _ in range(10):
        agent.update(3600.0, sim.world, [0.0] * 6, 1)
    alone = agent.isolation
    agent.nearest_peer_m = 2.0
    for _ in range(4):
        agent.update(3600.0, sim.world, [0.0] * 6, 2)
    together = agent.isolation
    return _check(
        "biology/social-drive-homeostatic",
        alone > 0.1 and together < alone,
        isolation_after_10h_alone=round(alone, 4),
        isolation_after_4h_with_peer=round(together, 4),
        relief_per_day=agent.isolation_relief_per_day,
    )


def check_shaping_attribution():
    """Dense shaping pays for a drink immediately, not at death."""
    cfg = _small_cfg(population=1)
    sim = Simulation(cfg)
    agent = sim.agents[0]
    agent.hydration = 0.5
    agent.pending = sim._reward_state(agent)
    agent.hydration = 0.6
    drink = sim._shaping_reward(agent)
    agent.pending = sim._reward_state(agent)
    drift = sim._shaping_reward(agent)
    return _check(
        "intelligence/dense-shaping-attribution",
        drink > 0.5 and drift < 0.0,
        drink_reward=round(drink, 4),
        no_change_reward=round(drift, 4),
        hydration_step=0.1,
    )


def check_reachability():
    cfg = _small_cfg(population=5)
    sim = Simulation(cfg)
    water = sim.reachability.get("water")
    return _check(
        "environment/reachability-measured-per-world",
        water is not None
        and sim.reachability.get("water_cells", 0) > 0
        and len(sim.reachability.get("water_per_house_m", [])) == 5,
        world_m=cfg.world_size_m,
        water_min_m=None if water is None else water["min_m"],
        water_median_m=None if water is None else water["median_m"],
        water_cells=sim.reachability.get("water_cells"),
        per_house_m=sim.reachability.get("water_per_house_m"),
    )


def check_sleep_physiology():
    """Sleep stays, but a sleeper wakes thirsty and bouts are capped."""
    cfg = _small_cfg(population=1)
    sim = Simulation(cfg)
    agent = sim.agents[0]
    agent.energy = 0.5
    agent.hydration = 0.5
    agent.sleeping = True
    agent.update(30.0, sim.world, [0.0] * 6, 1)
    woke_thirsty = not agent.sleeping

    agent.hydration = 1.0
    agent.nutrition = 1.0
    agent.energy = 0.5
    agent.sleeping = True
    agent.sleep_bout_s = 0.0
    slept = 0.0
    while agent.sleeping and slept < 6.0 * 3600.0:
        agent.update(60.0, sim.world, [0.0] * 6, 1)
        slept += 60.0
    capped = (not agent.sleeping) and slept <= SLEEP_BOUT_MAX_S + 120.0
    return _check(
        "biology/sleep-is-physiological",
        woke_thirsty and capped,
        woke_at_hydration=0.5,
        bout_length_s=slept,
        bout_cap_s=SLEEP_BOUT_MAX_S,
    )


def check_only_two_architectures():
    return _check(
        "architecture/two-inhabitant-architectures",
        BRAIN_KINDS == ("neural", "hybrid"),
        kinds=list(BRAIN_KINDS),
    )


CHECKS = (
    check_only_two_architectures,
    check_water_mass_conservation,
    check_shallow_water_dynamics,
    check_thermal_diffusion_conservation,
    check_thermal_ledger,
    check_free_fall_accuracy,
    check_ballistic_energy_drift,
    check_restitution,
    check_determinism,
    check_checkpoint_resume,
    check_population_setup,
    check_dawn_start,
    check_conspecific_channel,
    check_social_drive,
    check_sleep_physiology,
    check_shaping_attribution,
    check_reachability,
    check_prediction_learning,
    check_brain_parity,
    check_sensory_firewall,
    check_death_permanence,
    check_knowledge_transfer,
)


def run_all():
    return [check() for check in CHECKS]


def brief(result):
    parts = []
    for key, value in result["detail"].items():
        if isinstance(value, float):
            parts.append(f"{key}={value:.3g}")
        else:
            parts.append(f"{key}={value}")
    return " ".join(parts)
