"""The two permitted inhabitant architectures.

Only ``neural`` and ``hybrid`` brains exist. Both consume the identical
sensor vector and emit the identical 6-dimension action vector, which is what
makes their behaviour comparable on the same task.
"""

from .hybrid import HybridBrain
from .neural import OUTPUT_DIM, NeuralBrain

BRAIN_KINDS = ("neural", "hybrid")


def make_brain(kind, rng, cfg, label=None):
    if kind == "neural":
        return NeuralBrain(rng, hidden=cfg.hidden_units,
                           plasticity=cfg.plasticity,
                           novelty_weight=cfg.novelty_weight, label=label or kind)
    if kind == "hybrid":
        return HybridBrain(rng, hidden=cfg.hidden_units,
                           plasticity=cfg.plasticity,
                           novelty_weight=cfg.novelty_weight, label=label or kind)
    raise ValueError(f"unsupported brain kind: {kind}")


__all__ = ["BRAIN_KINDS", "HybridBrain", "NeuralBrain", "OUTPUT_DIM", "make_brain"]
