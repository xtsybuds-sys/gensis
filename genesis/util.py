"""Small numerical helpers shared across Genesis.

Deliberately stdlib-only so the simulation core runs on a bare Python 3.10+
interpreter with no install step and no paid services.
"""

from __future__ import annotations

import hashlib
import json
import math
from operator import mul

TAU = 2.0 * math.pi


def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v


def lerp(a, b, t):
    return a + (b - a) * t


def smoothstep(t):
    t = clamp(t, 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def dot(a, b):
    return sum(map(mul, a, b))


def matvec(matrix, vec):
    return [sum(map(mul, row, vec)) for row in matrix]


def mean(values):
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def norm(vec):
    return math.sqrt(sum(v * v for v in vec))


def normalize(obj):
    """Canonical JSON-safe form: sorted keys, -0.0 folded to 0.0."""
    if isinstance(obj, dict):
        return {str(k): normalize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [normalize(v) for v in obj]
    if isinstance(obj, float):
        return obj + 0.0
    if isinstance(obj, (int, str, bool)) or obj is None:
        return obj
    return repr(obj)


def stable_hash(obj):
    """Deterministic digest of a JSON-able structure (float repr preserved)."""
    payload = json.dumps(obj, sort_keys=True, default=repr, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def ema(previous, value, alpha):
    return value if previous is None else previous + alpha * (value - previous)
