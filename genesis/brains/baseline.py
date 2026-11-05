"""Random motor policy - a measurement baseline, not an inhabitant architecture.

This exists for one purpose: establishing whether the world is survivable at all.
If a random policy cannot survive either, the environment is invalid and no
learning comparison between the two real architectures means anything. It is
deliberately excluded from ``BRAIN_KINDS`` and is never spawned by default.
"""

from __future__ import annotations

from ..sensors import INPUT_DIM


class RandomPolicy:
    kind = "baseline-random"

    def __init__(self, rng, hidden=24, plasticity=0.0, novelty_weight=0.0,
                 label="random", w_scale=0.0, planner=True, **kwargs):
        self.rng = rng
        self.label = label
        self.hidden = 0
        self.input_dim = INPUT_DIM
        self.prediction_error = 0.0
        self.novelty = 0.0
        self.decisions = 0

    def act(self, x, ctx=None):
        self.decisions += 1
        return [self.rng.uniform(-1.0, 1.0) for _ in range(6)]

    def learn(self, reward, next_x):
        return self.stats()

    def consolidate(self):
        return 0

    def stats(self):
        return {
            "kind": self.kind,
            "label": self.label,
            "hidden": 0,
            "synapses": 0,
            "prediction_error": 0.0,
            "novelty": 0.0,
            "weight_norm": 0.0,
            "mean_reward": 0.0,
            "decisions": self.decisions,
        }

    def state_dict(self):
        return {"kind": self.kind, "label": self.label}

    def load(self, data):
        return None
