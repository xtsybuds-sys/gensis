"""Abiotic chemistry: replication and the first protocells.

Not a claim of consciousness. See docs/implementation/PROTOCELL_LIFE_CRITERION.md.
"""

from .protocell import ProtocellReactor, run_protocell
from .reactor import Reactor, analyse, run_abiotic

__all__ = [
    "ProtocellReactor",
    "Reactor",
    "analyse",
    "run_abiotic",
    "run_protocell",
]
