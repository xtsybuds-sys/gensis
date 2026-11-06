"""Abiotic chemistry baseline: monomers, strands, template replication.

Rules, fixed before any run (no placed life):

- The reactor starts with four monomer species, energy and nothing else. There are no
  strands at t = 0.
- Geochemistry adds energy and, from it, monomers.
- Monomers ligate into short strands; strands can join while they fit under MAX_LEN.
- A strand of at least MIN_TEMPLATE_LEN can template-copy when the complementary monomers
  and energy are available. The copy inherits the complement with a per-base mutation
  probability; copying the copy recovers the original.
- Strands hydrolyse back into monomers and the strand population is capped.

Nothing selects a sequence. Whether a self-sustaining replicating lineage establishes is
measured, not assumed. The thresholds below are pre-registered: a lineage counts as
established if it reaches LIFE_MIN_COPIES copies, holds at least two copies for
LIFE_MIN_SAMPLES consecutive samples, and has at least one one-base mutant neighbour.
That is chemical self-replication with heredity and variation - not a claim of life,
consciousness or civilization.
"""

from __future__ import annotations

import random
from collections import Counter

ALPHABET = 4
MAX_LEN = 10
MIN_TEMPLATE_LEN = 4
STRAND_CAP = 500
ENERGY_CAP = 1200.0
ENERGY_INFLUX = 8.0
MONOMER_FLUX = 0.8
MONOMER_ENERGY = 0.25
EVENTS_PER_TICK = 24
MUTATION_RATE = 0.02
COMPLEMENT = (3, 2, 1, 0)

REPLICATION_ENERGY = 0.6
LIGATION_ENERGY = 0.4
CLEAVAGE_ENERGY = 0.1

SAMPLE_EVERY = 200
LIFE_MIN_COPIES = 4
LIFE_MIN_SAMPLES = 10


class Reactor:
    def __init__(self, seed, replication=True):
        self.rng = random.Random(seed)
        self.replication = replication
        self.monomers = [48, 48, 48, 48]
        self.energy = 300.0
        self.strands = []
        self.tick = 0
        self.births = 0
        self.first_strand = None
        self.first_replication = None

    # ------------------------------------------------------------------ events
    def _add_strand(self, sequence):
        if len(self.strands) >= STRAND_CAP:
            return False
        self.strands.append(sequence)
        if self.first_strand is None:
            self.first_strand = self.tick
        return True

    def _take_monomer(self):
        available = [b for b in range(ALPHABET) if self.monomers[b] > 0]
        if not available:
            return None
        base = self.rng.choice(available)
        self.monomers[base] -= 1
        return base

    def _replicate(self):
        if not self.replication or not self.strands:
            return False
        candidates = [s for s in self.strands if len(s) >= MIN_TEMPLATE_LEN]
        if not candidates:
            return False
        template = self.rng.choice(candidates)
        copied = [COMPLEMENT[base] for base in template]
        if sum(self.monomers[base] for base in copied) < len(copied):
            return False
        if self.energy < len(copied) * REPLICATION_ENERGY:
            return False
        for base in copied:
            self.monomers[base] -= 1
        self.energy -= len(copied) * REPLICATION_ENERGY
        child = tuple(
            self.rng.randrange(ALPHABET) if self.rng.random() < MUTATION_RATE else base
            for base in copied
        )
        if not self._add_strand(child):
            for base in child:
                self.monomers[base] += 1
            return False
        self.births += 1
        if self.first_replication is None:
            self.first_replication = self.tick
        return True

    def _ligate(self):
        if self.energy < LIGATION_ENERGY:
            return False
        if self.rng.random() < 0.5 or len(self.strands) < 2:
            if sum(self.monomers) < 2:
                return False
            left = self._take_monomer()
            right = self._take_monomer()
            if left is None or right is None:
                return False
            self.energy -= LIGATION_ENERGY
            self._add_strand((left, right))
            return True
        i = self.rng.randrange(len(self.strands))
        j = self.rng.randrange(len(self.strands))
        if i == j:
            return False
        left = self.strands[i]
        right = self.strands[j]
        if len(left) + len(right) > MAX_LEN:
            return False
        if len(self.strands) >= STRAND_CAP:
            return False
        for index in sorted((i, j), reverse=True):
            self.strands.pop(index)
        self.energy -= LIGATION_ENERGY
        self._add_strand(left + right)
        return True

    def _cleave(self):
        if not self.strands or self.energy < CLEAVAGE_ENERGY:
            return False
        index = self.rng.randrange(len(self.strands))
        sequence = self.strands[index]
        if len(sequence) < 2:
            return False
        if len(self.strands) + 1 >= STRAND_CAP:
            return False
        self.strands.pop(index)
        cut = self.rng.randrange(1, len(sequence))
        self.energy -= CLEAVAGE_ENERGY
        self._add_strand(sequence[:cut])
        self._add_strand(sequence[cut:])
        return True

    def _decay(self):
        if not self.strands:
            return False
        index = self.rng.randrange(len(self.strands))
        sequence = self.strands.pop(index)
        for base in sequence:
            self.monomers[base] += 1
        return True

    def _geochemistry(self):
        self.energy = min(ENERGY_CAP, self.energy + ENERGY_INFLUX)
        for base in range(ALPHABET):
            if self.energy >= MONOMER_ENERGY and self.rng.random() < MONOMER_FLUX:
                self.monomers[base] += 1
                self.energy -= MONOMER_ENERGY

    def step(self, geochemistry=True):
        if geochemistry:
            self._geochemistry()
        for _ in range(EVENTS_PER_TICK):
            roll = self.rng.random()
            if roll < 0.45:
                self._replicate()
            elif roll < 0.70:
                self._ligate()
            elif roll < 0.88:
                self._cleave()
            else:
                self._decay()
        self.tick += 1


def _hamming(left, right):
    if len(left) != len(right):
        return 99
    return sum(1 for a, b in zip(left, right) if a != b)


def _sequence_text(sequence):
    return "".join("ACGU"[base] for base in sequence)


def analyse(samples, sample_every=SAMPLE_EVERY, start_sample=0):
    """Find the most persistent lineage and its one-base mutants."""
    sequences = {}
    for index, counts in enumerate(samples):
        if index < start_sample:
            continue
        for sequence, count in counts.items():
            info = sequences.setdefault(
                sequence, {"max_copies": 0, "run": 0, "best_run": 0, "first_sample": index}
            )
            if count > info["max_copies"]:
                info["max_copies"] = count
            if count >= 2:
                info["run"] += 1
                if info["run"] > info["best_run"]:
                    info["best_run"] = info["run"]
            else:
                info["run"] = 0
    if not sequences:
        return {
            "sequences": 0,
            "dominant": None,
            "max_copies": 0,
            "persistence_ticks": 0,
            "mutant_neighbours": 0,
            "established": False,
            "evidence": "no strands formed after the first replication event",
        }
    dominant = max(
        sequences,
        key=lambda sequence: (sequences[sequence]["max_copies"], sequences[sequence]["best_run"]),
    )
    neighbours = [
        sequence for sequence in sequences
        if sequence != dominant and _hamming(sequence, dominant) == 1
    ]
    best = sequences[dominant]
    established = (
        best["max_copies"] >= LIFE_MIN_COPIES
        and best["best_run"] >= LIFE_MIN_SAMPLES
        and len(neighbours) >= 1
    )
    return {
        "sequences": len(sequences),
        "dominant": _sequence_text(dominant),
        "dominant_length": len(dominant),
        "max_copies": best["max_copies"],
        "persistence_ticks": best["best_run"] * sample_every,
        "mutant_neighbours": len(neighbours),
        "established": established,
        "evidence": (
            f"{best['max_copies']} copies, {best['best_run'] * sample_every} ticks at >=2 copies, "
            f"{len(neighbours)} one-base mutants"
        ),
    }


def run_abiotic(seed, ticks=60000, sample_every=SAMPLE_EVERY, replication=True):
    reactor = Reactor(seed, replication=replication)
    samples = []
    for _ in range(ticks):
        reactor.step()
        if reactor.tick % sample_every == 0:
            samples.append(Counter(reactor.strands))
    if reactor.first_replication is None:
        start_sample = len(samples)
    else:
        start_sample = min(len(samples), reactor.first_replication // sample_every)
    summary = analyse(samples, sample_every, start_sample=start_sample)
    summary["scored_from_sample"] = start_sample
    return {
        "seed": seed,
        "ticks": ticks,
        "replication_enabled": replication,
        "strands": len(reactor.strands),
        "births": reactor.births,
        "first_strand_tick": reactor.first_strand,
        "first_replication_tick": reactor.first_replication,
        "energy": round(reactor.energy, 2),
        "monomers": list(reactor.monomers),
        **summary,
    }


def format_table(rows):
    if not rows:
        return "(no rows)"
    header = (
        f"{'seed':<10}{'ticks':>8}{'strands':>8}{'births':>8}{'first':>8}"
        f"{'firstrep':>10}{'copies':>8}{'persist':>9}{'mut':>5}{'est':>5}"
    )
    lines = [header, "-" * len(header)]
    for row in rows:
        lines.append(
            f"{row['seed']:<10}{row['ticks']:>8}{row['strands']:>8}{row['births']:>8}"
            f"{str(row['first_strand_tick']):>8}{str(row['first_replication_tick']):>10}"
            f"{row['max_copies']:>8}{row['persistence_ticks']:>9}"
            f"{row['mutant_neighbours']:>5} {str(row['established']):>5}"
        )
    return "\n".join(lines)
