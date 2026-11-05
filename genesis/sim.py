"""Simulation orchestrator: world, inhabitants, social layer, persistence."""

from __future__ import annotations

import math
import pickle
import random

from .agents import Inhabitant
from .brains import make_brain
from .brains.hybrid import HybridBrain
from .physics import PhysicsWorld
from .sensors import sense
from .util import TAU, mean, normalize, stable_hash

NAMES = ("Aster", "Brann", "Coral", "Dune", "Echo", "Fenn", "Gale", "Hollow")
ENCOUNTER_RANGE_M = 25.0
REWARD_SCALE = 40.0


class Simulation:
    def __init__(self, cfg, store=None):
        self.cfg = cfg
        self.store = store
        self.rng = random.Random(cfg.seed)
        self.world = PhysicsWorld(cfg, self.rng)
        self.tick = 0
        self.agents = []
        self.relationships = {}
        self.encounters = 0
        self.discoveries = []
        self.water_sources = {}
        self.food_sources = {}
        self.knowledge_links = []
        self.metrics_history = []
        self.recent_events = []
        self.deaths = 0
        self.checkpoint_count = 0
        if cfg.population:
            self._populate()
        if self.store is not None:
            self.store.meta("config", cfg.to_dict())
            self.store.meta("seed", cfg.seed)
            self.store.commit()

    # -- initialization ---------------------------------------------------
    def _suitable(self, i, j):
        if self.world.terrain.heights[j][i] < self.cfg.water_level_m + 2.5:
            return False
        x, y = self.world.terrain.cell_centre(i, j)
        return self.world.terrain.slope_magnitude(x, y) < 0.30

    def _choose_homes(self, count):
        """Pick separated, buildable sites: five separate houses."""
        n = self.cfg.grid
        candidates = [
            (i, j) for j in range(n) for i in range(n) if self._suitable(i, j)
        ]
        if not candidates:
            candidates = [(n // 2, n // 2)]
        self.rng.shuffle(candidates)
        chosen = [candidates[0]]
        base_gap = self.cfg.world_size_m * 0.28
        for factor in (1.0, 0.6, 0.3, 0.12):
            gap = base_gap * factor
            for cell in candidates:
                if len(chosen) >= count:
                    break
                x, y = self.world.terrain.cell_centre(*cell)
                if all(
                    math.hypot(
                        x - self.world.terrain.cell_centre(*c)[0],
                        y - self.world.terrain.cell_centre(*c)[1],
                    )
                    >= gap
                    for c in chosen
                ):
                    chosen.append(cell)
            if len(chosen) >= count:
                break
        while len(chosen) < count:
            chosen.append(candidates[len(chosen) % len(candidates)])
        return [
            (cell, self.world.terrain.cell_centre(*cell)) for cell in chosen[:count]
        ]

    def _populate(self):
        sites = self._choose_homes(self.cfg.population)
        for index, (cell, position) in enumerate(sites):
            kind = "neural" if index % 2 == 0 else "hybrid"
            name = NAMES[index % len(NAMES)]
            brain = make_brain(kind, self.rng, self.cfg, label=f"{name}/{kind}")
            agent = Inhabitant(
                index + 1,
                name,
                brain,
                position,
                heading=self.rng.uniform(0.0, TAU),
                home_cell=cell,
            )
            self.agents.append(agent)
            if self.store is not None:
                self.store.agent(agent, self.tick)
            self._record(
                "spawn",
                agent.name,
                {
                    "brain": kind,
                    "pos": [round(v, 1) for v in position],
                    "home_cell": list(cell),
                },
            )

    # -- bookkeeping ------------------------------------------------------
    def _record(self, kind, agent=None, detail=None):
        entry = {"tick": self.tick, "kind": kind, "agent": agent, "detail": detail or {}}
        self.recent_events.append(entry)
        if len(self.recent_events) > 400:
            del self.recent_events[:200]
        if self.store is not None:
            self.store.event(self.tick, kind, agent, detail)

    def _discovery(self, kind, cell, agent, detail=None):
        entry = {
            "tick": self.tick,
            "kind": kind,
            "cell": list(cell),
            "agent": agent.name,
            "detail": detail or {},
        }
        self.discoveries.append(entry)
        if self.store is not None:
            self.store.discovery(self.tick, kind, cell, agent.name, detail)

    def _teach(self, agent, token, cell, kind):
        brain = agent.brain
        if not isinstance(brain, HybridBrain):
            return False
        if token in brain.tokens:
            return False
        brain.tokens.add(token)
        brain.remember_place(cell[0], cell[1], kind)
        return True

    # -- the step ---------------------------------------------------------
    def step(self):
        cfg = self.cfg
        tick = self.tick + 1
        dt = cfg.tick_seconds
        self.tick = tick
        self.world.step(dt, tick)

        for agent in self.agents:
            if not agent.alive:
                continue
            events = agent.update(dt, self.world, agent.last_actions, tick)
            if "drank" in events:
                self._note_source(agent, events["drank"], "water")
            if "ate" in events:
                self._note_source(agent, events["ate"], "food")
            if events.get("woke"):
                replayed = agent.brain.consolidate()
                self._record(
                    "wake",
                    agent.name,
                    {
                        "slept_h": round(agent.sleep_seconds / 3600.0, 2),
                        "replays": replayed,
                    },
                )
            if events.get("died"):
                self.deaths += 1
                self._record(
                    "death",
                    agent.name,
                    {
                        "age_days": round(agent.age_s / 86400.0, 2),
                        "hydration": round(agent.hydration, 3),
                        "nutrition": round(agent.nutrition, 3),
                    },
                )
                if self.store is not None:
                    self.store.agent(agent, tick)

        if tick % cfg.decision_every == 0:
            for agent in self.agents:
                if agent.alive:
                    self._decide(agent, tick)
        if tick % (cfg.decision_every * 2) == 0:
            self._social(tick)

        if cfg.log_every and tick % cfg.log_every == 0:
            self._log_metrics(tick)
        if cfg.checkpoint_every and tick % cfg.checkpoint_every == 0:
            self.checkpoint()
        return tick

    def _decide(self, agent, tick):
        if tick % self.cfg.sense_every == 0 or not agent.sensors:
            vector, frame = sense(agent, self.world)
            agent.sensors = vector
            agent.frame = frame
        vector = agent.sensors

        if agent.pending is not None:
            reward = (agent.wellbeing - agent.pending) * REWARD_SCALE
            agent.brain.learn(reward, vector)

        actions = agent.brain.act(
            vector,
            {"tick": tick, "heading": agent.heading, "pos": list(agent.pos)},
        )
        agent.last_actions = actions
        agent.pending = agent.wellbeing

    # -- social layer -----------------------------------------------------
    def _social(self, tick):
        alive = [a for a in self.agents if a.alive]
        for i in range(len(alive)):
            for j in range(i + 1, len(alive)):
                a = alive[i]
                b = alive[j]
                distance = math.hypot(a.pos[0] - b.pos[0], a.pos[1] - b.pos[1])
                if distance > ENCOUNTER_RANGE_M:
                    continue
                key = (a.aid, b.aid)
                first = key not in self.relationships
                self.relationships[key] = self.relationships.get(key, 0) + 1
                self.encounters += 1
                if first:
                    self._record(
                        "encounter",
                        a.name,
                        {
                            "with": b.name,
                            "distance_m": round(distance, 1),
                            "clock": self.world.clock(),
                        },
                    )
                self._exchange(a, b, tick)

    def _exchange(self, a, b, tick):
        for sender, receiver in ((a, b), (b, a)):
            brain = sender.brain
            if not isinstance(brain, HybridBrain):
                continue
            shared = brain.share_with(receiver.brain)
            for token in shared:
                self.knowledge_links.append(
                    {"tick": tick, "token": token, "from": sender.name, "to": receiver.name}
                )
                if self.store is not None:
                    self.store.knowledge(tick, token, sender.name, receiver.name)
            if shared:
                self._record(
                    "knowledge_transfer",
                    sender.name,
                    {"to": receiver.name, "tokens": shared},
                )

    def _note_source(self, agent, cell, kind):
        key = f"{cell[0]},{cell[1]}"
        registry = self.water_sources if kind == "water" else self.food_sources
        token = f"{kind}:{key}"
        if key not in registry:
            registry[key] = {"tick": self.tick, "agent": agent.name}
            detail = {"agent": agent.name, "clock": self.world.clock()}
            if kind == "water":
                detail["depth_m"] = round(self.world.water_depth_at(*agent.pos), 2)
            else:
                detail["biomass"] = round(self.world.biomass_at(*agent.pos), 3)
            self._discovery(f"{kind}_source", cell, agent, detail)
        if self._teach(agent, token, cell, kind):
            self._record("concept", agent.name, {"token": token})

    # -- reporting --------------------------------------------------------
    def snapshot(self):
        alive = [a for a in self.agents if a.alive]
        cell_area = self.world.terrain.cell_m ** 2
        return {
            "tick": self.tick,
            "clock": self.world.clock(),
            "alive": len(alive),
            "population": len(self.agents),
            "deaths": self.deaths,
            "sleeping": sum(1 for a in alive if a.sleeping),
            "mean_energy": round(mean(a.energy for a in alive), 3),
            "mean_hydration": round(mean(a.hydration for a in alive), 3),
            "mean_nutrition": round(mean(a.nutrition for a in alive), 3),
            "mean_health": round(mean(a.health for a in alive), 3),
            "mean_prediction_error": round(
                mean(a.brain.prediction_error for a in alive), 5
            ),
            "mean_distance_m": round(mean(a.distance_m for a in alive), 1),
            "encounters": self.encounters,
            "discoveries": len(self.discoveries),
            "water_sources": len(self.water_sources),
            "food_sources": len(self.food_sources),
            "knowledge_links": len(self.knowledge_links),
            "tokens": sum(
                len(a.brain.tokens)
                for a in alive
                if isinstance(a.brain, HybridBrain)
            ),
            "water_m3": round(self.world.water.volume(cell_area), 1),
            "biomass": round(self.world.plants.total(), 2),
            "light": round(self.world.light(), 3),
        }

    def _log_metrics(self, tick):
        data = self.snapshot()
        self.metrics_history.append(data)
        if self.store is not None:
            self.store.metric(tick, data)

    def dashboard(self):
        return {
            "status": self.snapshot(),
            "world": self.world.summary(),
            "conservation": self.world.conservation(),
            "population": [a.stats() for a in self.agents],
            "relationships": [
                {"a": k[0], "b": k[1], "encounters": v}
                for k, v in sorted(self.relationships.items())
            ],
            "discoveries": self.discoveries[-40:],
            "events": self.recent_events[-40:],
            "metrics": self.metrics_history[-120:],
            "homes": [list(a.home_cell) for a in self.agents],
        }

    def report(self):
        alive = [a for a in self.agents if a.alive]
        snap = self.snapshot()
        conservation = self.world.conservation()
        first = next(
            (e for e in self.recent_events if e["kind"] == "encounter"), None
        )
        per_agent = []
        for agent in self.agents:
            per_agent.append(
                {
                    "name": agent.name,
                    "brain": agent.brain.kind,
                    "alive": agent.alive,
                    "distance_m": round(agent.distance_m, 1),
                    "drinks": agent.drinks,
                    "meals": agent.meals,
                    "sleep_h": round(agent.sleep_seconds / 3600.0, 2),
                    "prediction_error": agent.brain.stats()["prediction_error"],
                    "skills": agent.brain.stats().get("tokens", 0),
                }
            )
        return {
            "config": self.cfg.to_dict(),
            "world_days": round(self.cfg.tick_count * self.cfg.tick_seconds / 86400.0, 3),
            "ticks": self.tick,
            "alive": len(alive),
            "deaths": self.deaths,
            "snapshot": snap,
            "conservation": conservation,
            "agents": per_agent,
            "encounters": self.encounters,
            "first_encounter": first,
            "discoveries": len(self.discoveries),
            "knowledge_links": len(self.knowledge_links),
            "tokens": sum(
                len(a.brain.tokens) for a in self.agents if isinstance(a.brain, HybridBrain)
            ),
            "checkpoints": self.checkpoint_count,
        }

    # -- persistence ------------------------------------------------------
    def state(self):
        return {
            "cfg": self.cfg.to_dict(),
            "tick": self.tick,
            "rng": self.rng.getstate(),
            "world": self.world.state(),
            "agents": [a.state() for a in self.agents],
            "relationships": [[list(k), v] for k, v in self.relationships.items()],
            "encounters": self.encounters,
            "deaths": self.deaths,
            "discoveries": self.discoveries,
            "water_sources": self.water_sources,
            "food_sources": self.food_sources,
            "knowledge_links": self.knowledge_links[-400:],
            "metrics": self.metrics_history[-240:],
            "recent_events": self.recent_events[-200:],
        }

    def load_state(self, data):
        self.tick = data["tick"]
        self.rng.setstate(data["rng"])
        self.world.load_state(data["world"])
        self.agents = []
        for entry in data["agents"]:
            kind = entry["brain"]["kind"]
            brain = make_brain(kind, self.rng, self.cfg, label=entry["brain"].get("label"))
            agent = Inhabitant(
                entry["aid"],
                entry["name"],
                brain,
                entry["pos"],
                entry["heading"],
                entry["home_cell"],
            )
            agent.load(entry)
            self.agents.append(agent)
        self.relationships = {tuple(k): v for k, v in data["relationships"]}
        self.encounters = data["encounters"]
        self.deaths = data.get("deaths", 0)
        self.discoveries = data["discoveries"]
        self.water_sources = data.get("water_sources", {})
        self.food_sources = data.get("food_sources", {})
        self.knowledge_links = data["knowledge_links"]
        self.metrics_history = data["metrics"]
        self.recent_events = data["recent_events"]
        # Rebuilding brains draws from the RNG; restore it so a resumed run
        # continues the exact random stream the checkpoint captured.
        self.rng.setstate(data["rng"])

    def checkpoint(self):
        payload = pickle.dumps(self.state(), protocol=pickle.HIGHEST_PROTOCOL)
        if self.store is not None:
            self.store.checkpoint(self.tick, payload)
            self.store.commit()
        self.checkpoint_count += 1
        return len(payload)

    def digest(self):
        """Semantic state digest (sorted keys, -0.0 folded, no pickle framing)."""
        return stable_hash(normalize(self.state()))

    # -- running ----------------------------------------------------------
    def run(self, ticks=None, progress=None):
        target = self.cfg.tick_count if ticks is None else ticks
        start = self.tick
        while self.tick - start < target:
            self.step()
            if progress and self.tick % progress == 0:
                alive = sum(1 for a in self.agents if a.alive)
                print(
                    f"  tick {self.tick:6d}  {self.world.clock():<16} "
                    f"alive {alive}/{len(self.agents)}"
                )
        return self.report()
