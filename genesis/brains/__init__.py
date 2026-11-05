"""The two permitted inhabitant architectures, plus a measurement baseline.

``BRAIN_KINDS`` is the authoritative list of inhabitant architectures and stays
at exactly two. ``RandomPolicy`` is a benchmark arm used to validate whether the
world is survivable at all; it is never spawned by default and is not an
architecture under study.
"""

from .baseline import RandomPolicy
from .hybrid import HybridBrain
from .neural import OUTPUT_DIM, NeuralBrain

BRAIN_KINDS = ("neural", "hybrid")


def make_brain(kind, rng, cfg, label=None, genome=None):
    hidden = genome.hidden if genome is not None else cfg.hidden_units
    plasticity = genome.plasticity if genome is not None else cfg.plasticity
    novelty = genome.novelty_weight if genome is not None else cfg.novelty_weight
    w_scale = genome.w_scale if genome is not None else 0.45
    if kind == "neural":
        return NeuralBrain(
            rng,
            hidden=hidden,
            plasticity=plasticity,
            novelty_weight=novelty,
            label=label or kind,
            w_scale=w_scale,
        )
    if kind == "hybrid":
        return HybridBrain(
            rng,
            hidden=hidden,
            plasticity=plasticity,
            novelty_weight=novelty,
            label=label or kind,
            w_scale=w_scale,
            planner=cfg.planner,
        )
    if kind == "baseline-random":
        return RandomPolicy(rng, label=label or kind)
    raise ValueError(f"unsupported brain kind: {kind}")


__all__ = [
    "BRAIN_KINDS",
    "HybridBrain",
    "NeuralBrain",
    "OUTPUT_DIM",
    "RandomPolicy",
    "make_brain",
]
