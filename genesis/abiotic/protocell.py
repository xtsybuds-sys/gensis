"""Coarse-grained protocell chemistry: the first stage that can be called life.

The reactor starts with monomers, energy and nothing else. There are no strands, no
membranes and no cells at t = 0.

Rules, fixed before the validation runs:

- Geochemistry produces activated monomers and a slow abiotic supply of amphiphiles.
- Amphiphiles self-assemble into empty vesicles once their free concentration crosses a
  threshold. An empty vesicle is a compartment, not life.
- Inside a vesicle, monomers and strands ligate; strands hydrolyse. A strand is a catalyst
  if it begins with GG and is at least four bases long. The base after GG sets its
  catalytic efficiency: G or C is fast, A or U is slow. That is the heritable trait.
- A catalyst copies itself from monomers with a per-base mutation probability. Only
  catalysts replicate, so replication is not free for every strand.
- A catalyst also synthesises membrane lipid from monomers. A vesicle therefore grows only
  if its own catalysts work; there is no other lipid source for growth.
- A vesicle that reaches twice its assembly lipid content divides, splitting its strands
  between two daughters. Daughters inherit their catalysts; empty daughters can later
  acquire one by ligation, but that is not inheritance.
- Vesicles can lyse. Nothing is placed, selected or steered after t = 0.

The life criterion is in docs/implementation/PROTOCELL_LIFE_CRITERION.md. It requires all of:
origin without placement, replication, ten consecutive inherited catalyst generations,
metabolic lipid production, a persisting mutant, and a trait shift against a neutral control.
A chemical system that fails any of them is not called life here.

This is a coarse-grained model, not wet chemistry. It does not claim consciousness.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

ALPHABET = "ACGU"
BASE_INDEX = {base: index for index, base in enumerate(ALPHABET)}
G = BASE_INDEX["G"]
C = BASE_INDEX["C"]
A = BASE_INDEX["A"]
U = BASE_INDEX["U"]

MAX_LEN = 12
MIN_CATALYST_LEN = 4
STRAND_CAP = 100
VESICLE_LIPIDS = 20.0
DIVIDE_LIPIDS = 40.0
MAX_VESICLES = 120
SAMPLE_EVERY = 100

MONOMER_FLUX = 200.0
MONOMER_CAP = 10000.0
LIPID_FLUX = 0.08
LIPID_CAP = 400.0
LIPID_COST = 2.0

REPLICATION_RATE = 0.03
MUTATION_RATE = 0.02
CATALYST_LIPID_RATE = 0.01
LYSIS_RATE = 0.00008
LIGATION_EVENTS = 1
HYDROLYSIS_PROB = 0.15
HYDROLYSIS_MIN_LEN = 5

LIFE_MIN_GENERATIONS = 10
LIFE_MIN_TICKS = 5000
LIFE_MIN_MUTATION_AGE = 3
SELECTION_MIN_DELTA = 0.10
NEUTRAL_MAX_DELTA = 0.05


def is_catalyst(sequence):
    return len(sequence) >= MIN_CATALYST_LEN and sequence[0] == G and sequence[1] == G


def catalyst_trait(sequence):
    """GC fraction: a quantitative, heritable catalytic trait."""
    if not sequence:
        return 0.0
    return sum(1 for base in sequence if base in (G, C)) / len(sequence)


def efficiency(sequence, neutral=False):
    if neutral:
        return 1.0
    return 1.0 + 2.0 * catalyst_trait(sequence)


def hamming(left, right):
    if left is None or right is None or len(left) != len(right):
        return 99
    return sum(1 for a, b in zip(left, right) if a != b)


def sequence_text(sequence):
    return "".join(ALPHABET[base] for base in sequence)


@dataclass
class Lineage:
    id: int
    origin_tick: int
    first_catalyst_tick: int | None = None
    max_generation: int = 0
    max_catalyst_streak: int = 0
    max_mutation_age: int = 0
    divisions: int = 0
    catalyst_divisions: int = 0
    last_seen: int = 0


@dataclass
class Vesicle:
    lipids: float
    strands: dict[tuple, int]
    lineage: int
    generation: int
    born: int
    catalysts: dict[tuple, int]
    catalyst_total: int = 0
    total: int = 0
    catalyst_streak: int = 0
    mutation_age: int = 0
    dominant: tuple | None = None
    births: int = 0


def catalyst_count(vesicle):
    return vesicle.catalyst_total


def dominant_catalyst(vesicle):
    best = None
    best_count = 0
    for sequence, count in vesicle.catalysts.items():
        if count > best_count:
            best = sequence
            best_count = count
    return best


def strand_total(vesicle):
    return vesicle.total


def weighted_choice(rng, items, weights):
    total = sum(weights)
    if total <= 0:
        return None
    roll = rng.random() * total
    upto = 0.0
    for item, weight in zip(items, weights):
        upto += weight
        if roll <= upto:
            return item
    return items[-1]


class ProtocellReactor:
    """Warm little pond with membranes, catalysts and division."""

    def __init__(self, seed, catalysis=True, division=True, neutral=False,
                 max_vesicles=MAX_VESICLES):
        self.rng = random.Random(seed)
        self.catalysis = catalysis
        self.division = division
        self.neutral = neutral
        self.max_vesicles = max_vesicles
        self.sample_every = SAMPLE_EVERY

        self.monomers = float(4 * 120)
        self.lipids = 0.0
        self.vesicles: list[Vesicle] = []
        self.lineages: dict[int, Lineage] = {}
        self.next_lineage = 1
        self.tick = 0

        self.births = 0
        self.divisions = 0
        self.mutations = 0
        self.catalyst_lipid = 0.0
        self.first_strand_tick = None
        self.first_catalyst_tick = None
        self.first_replication_tick = None
        self.first_catalyst_sequence = None
        self.mutation_sequences = set()
        self.sequence_runs = {}
        self.sequence_best = {}
        self.samples = []

    # ------------------------------------------------------------------ resources
    def _consume_monomers(self, amount):
        if amount <= 0:
            return True
        if self.monomers + 1e-9 < amount:
            return False
        self.monomers -= amount
        return True

    def _add_strand(self, vesicle, sequence):
        if vesicle.total >= STRAND_CAP:
            return False
        vesicle.strands[sequence] = vesicle.strands.get(sequence, 0) + 1
        vesicle.total += 1
        if is_catalyst(sequence):
            vesicle.catalysts[sequence] = vesicle.catalysts.get(sequence, 0) + 1
            vesicle.catalyst_total += 1
            lineage = self.lineages[vesicle.lineage]
            if lineage.first_catalyst_tick is None:
                lineage.first_catalyst_tick = self.tick
            if self.first_catalyst_tick is None:
                self.first_catalyst_tick = self.tick
                self.first_catalyst_sequence = sequence
        if self.first_strand_tick is None:
            self.first_strand_tick = self.tick
        return True

    def _remove_strand(self, vesicle, sequence):
        count = vesicle.strands.get(sequence, 0)
        if count <= 0:
            return
        if count == 1:
            del vesicle.strands[sequence]
        else:
            vesicle.strands[sequence] = count - 1
        vesicle.total -= 1
        if is_catalyst(sequence):
            catalyst_count_here = vesicle.catalysts.get(sequence, 0)
            if catalyst_count_here <= 1:
                vesicle.catalysts.pop(sequence, None)
            else:
                vesicle.catalysts[sequence] = catalyst_count_here - 1
            vesicle.catalyst_total -= 1

    def _new_lineage(self):
        lineage = Lineage(id=self.next_lineage, origin_tick=self.tick, last_seen=self.tick)
        self.lineages[lineage.id] = lineage
        self.next_lineage += 1
        return lineage

    # ------------------------------------------------------------------ reactions
    def _replicate(self, vesicle):
        if not self.catalysis or vesicle.catalyst_total <= 0:
            return
        catalysts = list(vesicle.catalysts.items())
        weights = [count * efficiency(sequence, self.neutral)
                   for sequence, count in catalysts]
        total_weight = sum(weights)
        if total_weight <= 0:
            return
        resource = self.monomers / (self.monomers + 60.0)
        expected = REPLICATION_RATE * total_weight * resource
        births = int(expected)
        if self.rng.random() < expected - births:
            births += 1
        if births <= 0:
            return
        for _ in range(births):
            parent = weighted_choice(self.rng, [item[0] for item in catalysts], weights)
            if parent is None:
                return
            child = tuple(
                self.rng.randrange(4) if self.rng.random() < MUTATION_RATE else base
                for base in parent
            )
            if not self._consume_monomers(len(child)):
                return
            if not self._add_strand(vesicle, child):
                self.monomers += len(child)
                return
            vesicle.births += 1
            self.births += 1
            if child != parent:
                self.mutations += 1
                self.mutation_sequences.add(child)
            if self.first_replication_tick is None:
                self.first_replication_tick = self.tick

    def _ligate(self, vesicle):
        if vesicle.total >= STRAND_CAP:
            return
        if self.rng.random() < 0.5 or not vesicle.strands:
            if not self._consume_monomers(2):
                return
            sequence = (self.rng.randrange(4), self.rng.randrange(4))
            if not self._add_strand(vesicle, sequence):
                self.monomers += 2
            return
        strands = list(vesicle.strands)
        weights = [vesicle.strands[sequence] for sequence in strands]
        first = weighted_choice(self.rng, strands, weights)
        if first is None:
            return
        second = weighted_choice(self.rng, strands, weights)
        if second is None or len(first) + len(second) > MAX_LEN:
            return
        self._remove_strand(vesicle, first)
        self._remove_strand(vesicle, second)
        self._add_strand(vesicle, first + second)

    def _hydrolyse(self, vesicle):
        if not vesicle.strands or self.rng.random() > HYDROLYSIS_PROB:
            return
        strands = [sequence for sequence in vesicle.strands
                   if len(sequence) >= HYDROLYSIS_MIN_LEN]
        if not strands:
            return
        weights = [vesicle.strands[sequence] for sequence in strands]
        sequence = weighted_choice(self.rng, strands, weights)
        if sequence is None:
            return
        self._remove_strand(vesicle, sequence)
        if len(sequence) < 2:
            self.monomers += len(sequence)
            return
        cut = self.rng.randrange(1, len(sequence))
        left, right = sequence[:cut], sequence[cut:]
        for fragment in (left, right):
            if len(fragment) >= 2:
                self._add_strand(vesicle, fragment)
            else:
                self.monomers += len(fragment)

    def _grow(self, vesicle):
        if vesicle.catalyst_total <= 0:
            return
        produced = CATALYST_LIPID_RATE * sum(
            count * efficiency(sequence, self.neutral)
            for sequence, count in vesicle.catalysts.items()
        )
        cost = produced * LIPID_COST
        if self.monomers < cost:
            produced = max(0.0, self.monomers / LIPID_COST)
            cost = produced * LIPID_COST
        if produced <= 0:
            return
        self.monomers -= cost
        vesicle.lipids = min(DIVIDE_LIPIDS + 10.0, vesicle.lipids + produced)
        self.catalyst_lipid += produced

    def _split(self, vesicle):
        daughters = []
        parent_dominant = dominant_catalyst(vesicle)
        for _ in range(2):
            strands = {}
            catalysts = {}
            catalyst_total = 0
            total = 0
            for sequence, count in vesicle.strands.items():
                kept = sum(1 for _ in range(count) if self.rng.random() < 0.5)
                if not kept:
                    continue
                strands[sequence] = kept
                total += kept
                if is_catalyst(sequence):
                    catalysts[sequence] = kept
                    catalyst_total += kept
            daughter = Vesicle(
                lipids=vesicle.lipids / 2.0,
                strands=strands,
                lineage=vesicle.lineage,
                generation=vesicle.generation + 1,
                born=self.tick,
                catalysts=catalysts,
                catalyst_total=catalyst_total,
                total=total,
            )
            daughter.dominant = dominant_catalyst(daughter)
            if daughter.dominant is not None:
                daughter.catalyst_streak = vesicle.catalyst_streak + 1
            if daughter.dominant is not None and parent_dominant is not None:
                distance = hamming(parent_dominant, daughter.dominant)
                if distance == 1:
                    daughter.mutation_age = vesicle.mutation_age + 1
                elif distance == 0:
                    daughter.mutation_age = vesicle.mutation_age
            daughters.append(daughter)
        lineage = self.lineages[vesicle.lineage]
        lineage.divisions += 1
        lineage.last_seen = self.tick
        for daughter in daughters:
            lineage.max_generation = max(lineage.max_generation, daughter.generation)
            if daughter.catalyst_streak > 0:
                lineage.max_catalyst_streak = max(
                    lineage.max_catalyst_streak, daughter.catalyst_streak
                )
            lineage.max_mutation_age = max(lineage.max_mutation_age, daughter.mutation_age)
            if daughter.dominant is not None:
                lineage.catalyst_divisions += 1
        self.divisions += 1
        return daughters

    def _divide(self, vesicle):
        if not self.division or vesicle.lipids < DIVIDE_LIPIDS or not vesicle.strands:
            return False
        daughters = self._split(vesicle)
        if daughters is None:
            return False
        self.vesicles.remove(vesicle)
        self.vesicles.extend(daughters)
        if len(self.vesicles) > self.max_vesicles:
            empty = [candidate for candidate in self.vesicles
                     if candidate.catalyst_total == 0]
            pool = empty if empty else self.vesicles
            self.vesicles.remove(self.rng.choice(pool))
        return True

    def _lyse(self):
        if not self.vesicles:
            return
        for vesicle in list(self.vesicles):
            if self.rng.random() < LYSIS_RATE:
                self.vesicles.remove(vesicle)
                self.lipids = min(LIPID_CAP, self.lipids + vesicle.lipids)
                self.monomers += sum(len(sequence) * count
                                     for sequence, count in vesicle.strands.items())

    # ------------------------------------------------------------------ world
    def _geochemistry(self):
        self.monomers = min(MONOMER_CAP, self.monomers + MONOMER_FLUX)
        self.lipids = min(LIPID_CAP, self.lipids + LIPID_FLUX)

    def _assemble(self):
        while self.lipids >= VESICLE_LIPIDS and len(self.vesicles) < self.max_vesicles:
            self.lipids -= VESICLE_LIPIDS
            lineage = self._new_lineage()
            self.vesicles.append(Vesicle(
                lipids=VESICLE_LIPIDS,
                strands={},
                lineage=lineage.id,
                generation=0,
                born=self.tick,
                catalysts={},
            ))

    def step(self):
        self._geochemistry()
        self._assemble()
        for vesicle in list(self.vesicles):
            if vesicle not in self.vesicles:
                continue
            self._grow(vesicle)
            self._replicate(vesicle)
            for _ in range(LIGATION_EVENTS):
                self._ligate(vesicle)
            self._hydrolyse(vesicle)
            self._divide(vesicle)
            self.lineages[vesicle.lineage].last_seen = self.tick
        self._lyse()
        self.tick += 1

    # ------------------------------------------------------------------ measurement
    def _catalyst_sequences(self):
        for vesicle in self.vesicles:
            for sequence, count in vesicle.catalysts.items():
                yield sequence, count

    def sample(self):
        catalysts = list(self._catalyst_sequences())
        copies = sum(count for _, count in catalysts)
        trait_sum = sum(count * catalyst_trait(sequence) for sequence, count in catalysts)
        present = {sequence for sequence, _ in catalysts}
        for sequence in present:
            self.sequence_runs[sequence] = self.sequence_runs.get(sequence, 0) + 1
            self.sequence_best[sequence] = max(
                self.sequence_best.get(sequence, 0), self.sequence_runs[sequence]
            )
        for sequence in list(self.sequence_runs):
            if sequence not in present:
                self.sequence_runs[sequence] = 0
        mutant_best = max(
            (self.sequence_best.get(sequence, 0) for sequence in self.mutation_sequences),
            default=0,
        )
        best = None
        if self.lineages:
            best = max(
                self.lineages.values(),
                key=lambda item: (item.max_catalyst_streak, item.max_generation,
                                  item.divisions),
            )
        sample = {
            "tick": self.tick,
            "vesicles": len(self.vesicles),
            "with_catalyst": sum(1 for vesicle in self.vesicles
                                 if vesicle.catalyst_total > 0),
            "catalyst_copies": copies,
            "trait": (trait_sum / copies) if copies else None,
            "births": self.births,
            "divisions": self.divisions,
            "mutations": self.mutations,
            "catalyst_lipid": round(self.catalyst_lipid, 2),
            "max_generation": best.max_generation if best else 0,
            "max_streak": best.max_catalyst_streak if best else 0,
            "max_mutation_age": best.max_mutation_age if best else 0,
            "mutant_persistence_samples": mutant_best,
            "distinct_catalysts": len(present),
        }
        self.samples.append(sample)
        return sample

    def summary(self):
        best = None
        if self.lineages:
            best = max(
                self.lineages.values(),
                key=lambda item: (item.max_catalyst_streak, item.max_generation,
                                  item.divisions),
            )
        traits = [sample["trait"] for sample in self.samples if sample["trait"] is not None]
        window = max(1, len(traits) // 10)
        first = sum(traits[:window]) / len(traits[:window]) if traits else None
        last = sum(traits[-window:]) / len(traits[-window:]) if traits else None
        delta = (last - first) if first is not None and last is not None else None
        mutant_samples = max(
            (sample["mutant_persistence_samples"] for sample in self.samples), default=0
        )
        established = bool(
            best is not None
            and best.first_catalyst_tick is not None
            and best.max_catalyst_streak >= LIFE_MIN_GENERATIONS
            and best.max_generation >= LIFE_MIN_GENERATIONS
            and best.divisions >= LIFE_MIN_GENERATIONS
            and self.births > 0
            and self.catalyst_lipid > 0
            and (self.tick - best.first_catalyst_tick) >= LIFE_MIN_TICKS
            and self.mutations > 0
            and mutant_samples * self.sample_every >= 1000
        )
        return {
            "tick": self.tick,
            "first_strand_tick": self.first_strand_tick,
            "first_catalyst_tick": self.first_catalyst_tick,
            "first_replication_tick": self.first_replication_tick,
            "births": self.births,
            "divisions": self.divisions,
            "mutations": self.mutations,
            "catalyst_lipid": round(self.catalyst_lipid, 2),
            "vesicles": len(self.vesicles),
            "lineages": len(self.lineages),
            "best_lineage": best.id if best else None,
            "best_first_catalyst_tick": best.first_catalyst_tick if best else None,
            "best_max_generation": best.max_generation if best else 0,
            "best_max_catalyst_streak": best.max_catalyst_streak if best else 0,
            "best_max_mutation_age": best.max_mutation_age if best else 0,
            "best_divisions": best.divisions if best else 0,
            "best_catalyst_divisions": best.catalyst_divisions if best else 0,
            "trait_first": first,
            "trait_last": last,
            "trait_delta": delta,
            "mutant_persistence_samples": mutant_samples,
            "mutant_persistence_ticks": mutant_samples * self.sample_every,
            "mutant_sequences_seen": len(self.mutation_sequences),
            "established": established,
        }


def run_protocell(seed, ticks=20000, sample_every=SAMPLE_EVERY, catalysis=True,
                  division=True, neutral=False):
    reactor = ProtocellReactor(seed, catalysis=catalysis, division=division,
                               neutral=neutral)
    reactor.sample_every = sample_every
    for _ in range(ticks):
        reactor.step()
        if reactor.tick % sample_every == 0:
            reactor.sample()
    return reactor.summary()


if __name__ == "__main__":
    for seed in (1, 2):
        result = run_protocell(seed, ticks=3000, sample_every=300)
        print(result)
