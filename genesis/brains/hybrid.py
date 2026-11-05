"""Hybrid inhabitant: a neural core plus memory, planning and symbol sharing.

The neural core is the same network used by the pure-neural inhabitants and
receives the identical sensor vector. The extra components are internal state
only - an episodic buffer, bearing memory derived from its own past senses, a
drive-driven planner that biases (never replaces) the neural motor output, and
a symbolic token layer used for knowledge exchange with other inhabitants.
"""

from __future__ import annotations

import math

from ..sensors import (
    ISOLATION_INDEX,
    PEER_BEARING_COS_INDEX,
    PEER_BEARING_SIN_INDEX,
    PEER_PROXIMITY_INDEX,
)
from ..util import TAU, clamp
from .neural import NeuralBrain

RAY_COUNT = 8
CODE_WATER = 0.33
CODE_PLANT = 0.66

# Planner steering test (Muse decision 3, 2026-11-05).
VOTE_CONFIDENCE = 0.15
HYSTERESIS_RAD = 0.6
COMMIT_DECISIONS = 3


def _wrap(angle):
    while angle > math.pi:
        angle -= TAU
    while angle < -math.pi:
        angle += TAU
    return angle


class HybridBrain(NeuralBrain):
    kind = "hybrid"

    def __init__(self, rng, hidden=24, plasticity=0.02, novelty_weight=0.35,
                 label="hybrid", w_scale=0.45, planner=True):
        super().__init__(rng, hidden, plasticity, novelty_weight, label,
                         w_scale=w_scale)
        self.planner_enabled = bool(planner)
        self.water_votes = [0.0] * RAY_COUNT
        self.food_votes = [0.0] * RAY_COUNT
        self.episodes = []
        self.max_episodes = 200
        self.tokens = set()
        self.known_places = {}
        self.tick = 0
        self.signals = 0
        self.transfers = 0
        self.replays = 0
        self._last_out = [0.0] * 6
        self._last_x = None
        self.water_bearing = None
        self.food_bearing = None
        self.plan_uses = 0
        self.plan_target = None
        self.committed_bearing = None
        self.commit_left = 0

    # -- acting -----------------------------------------------------------
    def act(self, x, ctx=None):
        ctx = ctx or {}
        self.tick = ctx.get("tick", 0)
        out = super().act(x, ctx)
        self._update_votes(x)
        plan = self._plan(x, ctx.get("heading", 0.0)) if self.planner_enabled else None
        if plan is not None:
            forward, turn = plan
            self.plan_uses += 1
            out[0] = clamp(0.65 * forward + 0.35 * out[0], -1.0, 1.0)
            out[1] = clamp(0.75 * turn + 0.25 * out[1], -1.0, 1.0)
        if out[5] > 0.45:
            self.signals += 1
        self._last_out = list(out)
        self._last_x = list(x)
        return out

    def _update_votes(self, x):
        for r in range(RAY_COUNT):
            proximity = x[r]
            code = x[8 + r]
            if code == CODE_WATER:
                self.water_votes[r] = self.water_votes[r] * 0.85 + proximity
            else:
                self.water_votes[r] *= 0.97
            if code == CODE_PLANT:
                self.food_votes[r] = self.food_votes[r] * 0.85 + proximity
            else:
                self.food_votes[r] *= 0.97

    def _decay_memory(self):
        if self.water_bearing is not None:
            self.water_bearing *= 0.995
        if self.food_bearing is not None:
            self.food_bearing *= 0.995

    def _vote_direction(self, votes):
        """Vector sum of per-ray votes; returns (bearing, confidence).

        Multi-ray voting (Muse decision 3): several rays that see the same shore
        combine into one bearing, so a wide bank outvotes a single dim hit. The old
        planner took the argmax of one best ray, which dithers between near-equal
        rays and throws away the rest of what the inhabitant can see.
        """
        vx = 0.0
        vy = 0.0
        total = 0.0
        for r in range(RAY_COUNT):
            weight = votes[r]
            if weight <= 0.0:
                continue
            angle = r * (TAU / RAY_COUNT)
            vx += weight * math.cos(angle)
            vy += weight * math.sin(angle)
            total += weight
        if total <= 0.0:
            return None, 0.0
        return _wrap(math.atan2(vy, vx)), total

    def _apply_hysteresis(self, target):
        """Hold a chosen bearing for a few decisions instead of re-picking each one."""
        if (
            self.committed_bearing is not None
            and self.commit_left > 0
            and abs(_wrap(target - self.committed_bearing)) < HYSTERESIS_RAD
        ):
            self.commit_left -= 1
            return self.committed_bearing
        self.committed_bearing = target
        self.commit_left = COMMIT_DECISIONS
        return target

    def _plan(self, x, heading):
        """Drive-gated steering: biases the neural motor output, never replaces it.

        Two additions for the calibration sprint. First, memory: the relative
        bearing of the last sensible water/food ray is kept and decays, so a
        failed look no longer erases what the inhabitant already saw. The bearing
        came from its own sensors, so this is memory, not omniscience - and it is
        exactly the component a pure-neural brain does not have, which is what
        makes the planner ablation a real test rather than a formality.

        Second, the social drive: when isolation is high and nothing more urgent
        is missing, steer toward a perceived conspecific. Before the conspecific
        channel existed there was nothing to steer toward.
        """
        thirst = x[18]
        hunger = x[19]
        votes = None
        remembered = None
        if thirst >= 0.5:
            votes = self.water_votes
            remembered = "water"
        elif hunger >= 0.5:
            votes = self.food_votes
            remembered = "food"
        elif x[ISOLATION_INDEX] >= 0.6 and x[PEER_PROXIMITY_INDEX] > 0.02:
            bearing = math.atan2(
                x[PEER_BEARING_SIN_INDEX], x[PEER_BEARING_COS_INDEX]
            )
            turn = clamp(bearing * 1.6, -1.0, 1.0)
            forward = clamp(0.35 + 0.65 * math.cos(bearing), 0.1, 1.0)
            self.plan_target = "social"
            return forward, turn
        if votes is None:
            return None
        self._decay_memory()
        target, confidence = self._vote_direction(votes)
        if target is None or confidence < VOTE_CONFIDENCE:
            memory = (
                self.water_bearing if remembered == "water" else self.food_bearing
            )
            if memory is None:
                return None
            self.plan_target = remembered + "-memory"
            return 0.6, clamp(memory * 1.2, -1.0, 1.0)
        target = self._apply_hysteresis(target)
        if remembered == "water":
            self.water_bearing = target
        else:
            self.food_bearing = target
        self.plan_target = remembered
        turn = clamp(target * 1.6, -1.0, 1.0)
        forward = clamp(0.35 + 0.65 * math.cos(target), 0.1, 1.0)
        return forward, turn

    # -- learning ---------------------------------------------------------
    def learn(self, reward, next_x):
        if self._last_x is not None:
            self.episodes.append(
                {
                    "x": self._last_x,
                    "out": self._last_out,
                    "next": list(next_x),
                    "reward": reward,
                    "tick": self.tick,
                }
            )
            if len(self.episodes) > self.max_episodes:
                self.episodes.pop(0)
        return super().learn(reward, next_x)

    def consolidate(self):
        """Sleep replay: re-fit the world model on recent experience."""
        if not self.episodes:
            return 0
        sample = self.episodes[-50:]
        total = 0.0
        for episode in sample:
            total += self._lms(episode["x"], episode["next"])
        mean_err = total / len(sample)
        self.prediction_error = 0.5 * self.prediction_error + 0.5 * mean_err
        self.replays += len(sample)
        return len(sample)

    # -- knowledge --------------------------------------------------------
    def remember_place(self, i, j, kind):
        self.known_places[f"{i},{j}"] = kind

    def observation_token(self, x):
        """Derive a discrete label for a sensed situation (a proto-symbol)."""
        key = "s%d%d" % (int(round(x[16] * 3)), int(round(max(x[8:16]) * 3)))
        if key not in self.tokens:
            self.tokens.add(key)
            return key
        return None

    def share_with(self, other, limit=8):
        """Give a nearby brain tokens and a sample of remembered places."""
        if not isinstance(other, HybridBrain):
            return []
        shared = []
        for token in sorted(self.tokens):
            if token not in other.tokens:
                other.tokens.add(token)
                shared.append(token)
                if len(shared) >= limit:
                    break
        if self.known_places:
            keys = sorted(self.known_places)[:limit]
            for key in keys:
                other.known_places.setdefault(key, self.known_places[key])
        if shared:
            other.transfers += len(shared)
        return shared

    # -- introspection ----------------------------------------------------
    def stats(self):
        base = super().stats()
        base.update(
            {
                "episodes": len(self.episodes),
                "tokens": len(self.tokens),
                "known_places": len(self.known_places),
                "signals": self.signals,
                "transfers": self.transfers,
                "replays": self.replays,
                "plan_uses": self.plan_uses,
                "plan_target": self.plan_target,
            }
        )
        return base

    def state_dict(self):
        data = super().state_dict()
        data.update(
            {
                "water_votes": self.water_votes,
                "food_votes": self.food_votes,
                "episodes": self.episodes,
                "tokens": sorted(self.tokens),
                "known_places": self.known_places,
                "signals": self.signals,
                "transfers": self.transfers,
                "replays": self.replays,
                "plan_uses": self.plan_uses,
                "plan_target": self.plan_target,
                "water_bearing": self.water_bearing,
                "food_bearing": self.food_bearing,
                "committed_bearing": self.committed_bearing,
                "commit_left": self.commit_left,
                "last_x": self._last_x,
                "last_out": self._last_out,
                "tick": self.tick,
                "planner_enabled": self.planner_enabled,
            }
        )
        return data

    def load(self, data):
        super().load(data)
        self.water_votes = data["water_votes"]
        self.food_votes = data["food_votes"]
        self.episodes = data["episodes"]
        self.tokens = set(data["tokens"])
        self.known_places = data["known_places"]
        self.signals = data["signals"]
        self.transfers = data["transfers"]
        self.replays = data["replays"]
        self.plan_uses = data.get("plan_uses", 0)
        self.plan_target = data.get("plan_target")
        self.water_bearing = data.get("water_bearing")
        self.food_bearing = data.get("food_bearing")
        self.committed_bearing = data.get("committed_bearing")
        self.commit_left = data.get("commit_left", 0)
        self._last_x = data.get("last_x")
        self._last_out = data.get("last_out", [0.0] * 6)
        self.tick = data.get("tick", 0)
        self.planner_enabled = data.get("planner_enabled", True)
