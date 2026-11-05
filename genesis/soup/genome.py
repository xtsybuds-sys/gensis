"""The pilot genome: twelve genes, each with a declared range.

Ranges are part of the design, not tuning: a gene that mutates outside its range is
clamped, so no run can produce a cell with a negative speed or an unbounded size.
``mutation_modifier`` is itself a gene, so the mutation rate is selectable.
"""

from __future__ import annotations

import math

from ..util import clamp

# name, minimum, maximum, founding mean
GENES = (
    ("speed", 0.01, 0.40, 0.08),
    ("size", 0.5, 2.0, 1.0),
    ("nutrient_affinity", 0.0, 2.0, 1.0),
    ("light_affinity", 0.0, 2.0, 0.3),
    ("temperature_affinity", 0.0, 2.0, 0.2),
    ("efficiency", 0.2, 1.0, 0.55),
    ("division_threshold", 1.2, 4.0, 2.0),
    ("mutation_modifier", 0.001, 0.05, 0.01),
    ("adhesion", 0.0, 1.0, 0.1),
    ("sensor_range", 0.25, 3.0, 0.75),
    ("toxin_tolerance", 0.0, 1.0, 0.3),
    ("dormancy_threshold", 0.0, 1.0, 0.15),
)

GENE_NAMES = tuple(gene[0] for gene in GENES)
_INDEX = {name: i for i, name in enumerate(GENE_NAMES)}


class Genome:
    """A fixed-length vector of gene values that knows its own bounds."""

    __slots__ = ("values",)

    def __init__(self, values):
        if len(values) != len(GENES):
            raise ValueError(f"genome needs {len(GENES)} genes, got {len(values)}")
        self.values = [float(v) for v in values]

    @classmethod
    def founding(cls, rng, spread=0.05):
        """A founder drawn near each gene's midpoint value, not at the edge."""
        values = []
        for _, low, high, init in GENES:
            values.append(clamp(rng.gauss(init, spread * (high - low)), low, high))
        return cls(values)

    def get(self, name):
        return self.values[_INDEX[name]]

    def mutate(self, rng):
        """Copy with per-gene mutation; the rate comes from this genome."""
        rate = self.get("mutation_modifier")
        out = list(self.values)
        for i, (_, low, high, _) in enumerate(GENES):
            if rng.random() < rate:
                step = rng.gauss(0.0, 0.05 * (high - low))
                out[i] = clamp(out[i] + step, low, high)
        return Genome(out)

    def distance(self, other):
        """Normalized L2 distance, so traits with wide ranges do not dominate."""
        total = 0.0
        for i, (_, low, high, _) in enumerate(GENES):
            span = high - low
            delta = (self.values[i] - other.values[i]) / span
            total += delta * delta
        return math.sqrt(total)

    def to_dict(self):
        return {name: round(value, 6) for name, value in zip(GENE_NAMES, self.values)}
