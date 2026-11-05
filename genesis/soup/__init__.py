"""Primordial soup pilot: cells, mutation, and a bounded nutrient dish.

Approved by Muse on 2026-11-05 as strict nutrient-only competition (no predation).
The pilot measures whether complexity grows from mutation and selection on a simple
substrate; it is deliberately separate from the human-scale town kernel.
"""

from .dish import NutrientDish
from .genome import GENE_NAMES, GENES, Genome
from .pilot import evaluate, format_table, run_pilot

__all__ = [
    "GENE_NAMES",
    "GENES",
    "Genome",
    "NutrientDish",
    "evaluate",
    "format_table",
    "run_pilot",
]
