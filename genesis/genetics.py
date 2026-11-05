"""Heritable brain parameters.

A genome is the small set of values that shape how a brain is built and how fast
it learns. Inheritance is genetic only: a child starts with a mutated genome and a
fresh brain. What a child inherits behaviourally is knowledge tokens through the
social layer, not its parent's weights - that distinction matters when we later
claim that cumulative knowledge crossed a generation boundary.

Selection acts through reproduction, never through a fitness function that rewards
anything other than surviving and reproducing inside the world.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

from .util import clamp

HIDDEN_CHOICES = (12, 16, 24, 32)


@dataclass(frozen=True)
class Genome:
    brain_kind: str = "neural"
    hidden: int = 24
    plasticity: float = 0.02
    novelty_weight: float = 0.35
    w_scale: float = 0.45

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            brain_kind=data.get("brain_kind", "neural"),
            hidden=int(data.get("hidden", 24)),
            plasticity=float(data.get("plasticity", 0.02)),
            novelty_weight=float(data.get("novelty_weight", 0.35)),
            w_scale=float(data.get("w_scale", 0.45)),
        )

    @classmethod
    def random(cls, rng, kind="neural"):
        return cls(
            brain_kind=kind,
            hidden=rng.choice(HIDDEN_CHOICES),
            plasticity=clamp(rng.gauss(0.02, 0.006), 0.004, 0.06),
            novelty_weight=clamp(rng.gauss(0.35, 0.12), 0.0, 0.9),
            w_scale=clamp(rng.gauss(0.45, 0.10), 0.15, 0.9),
        )

    def mutate(self, rng, rate=1.0):
        rate = max(0.0, float(rate))
        hidden = self.hidden
        if rng.random() < 0.15 * rate:
            index = HIDDEN_CHOICES.index(hidden) if hidden in HIDDEN_CHOICES else 0
            step = rng.choice((-1, 1))
            hidden = HIDDEN_CHOICES[int(clamp(index + step, 0, len(HIDDEN_CHOICES) - 1))]
        return Genome(
            brain_kind=self.brain_kind,
            hidden=hidden,
            plasticity=clamp(self.plasticity + rng.gauss(0.0, 0.004 * rate), 0.004, 0.06),
            novelty_weight=clamp(
                self.novelty_weight + rng.gauss(0.0, 0.06 * rate), 0.0, 0.9
            ),
            w_scale=clamp(self.w_scale + rng.gauss(0.0, 0.05 * rate), 0.15, 0.9),
        )
