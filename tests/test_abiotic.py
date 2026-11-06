"""Tests for the abiotic chemistry baseline."""

from __future__ import annotations

import unittest
from collections import Counter

from genesis.abiotic.reactor import (
    COMPLEMENT,
    LIFE_MIN_COPIES,
    LIFE_MIN_SAMPLES,
    Reactor,
    analyse,
    run_abiotic,
)


def _bases(reactor):
    return sum(reactor.monomers) + sum(len(sequence) for sequence in reactor.strands)


class AbioticTests(unittest.TestCase):
    def test_no_life_is_placed_at_the_start(self):
        reactor = Reactor(1)
        self.assertEqual(reactor.strands, [])
        self.assertIsNone(reactor.first_strand)

    def test_bases_are_conserved_without_geochemistry(self):
        reactor = Reactor(3)
        for _ in range(200):
            reactor.step(geochemistry=False)
            self.assertEqual(_bases(reactor), 4 * 48)

    def test_complement_is_an_involution(self):
        for base in range(4):
            self.assertEqual(COMPLEMENT[COMPLEMENT[base]], base)

    def test_deterministic_for_a_seed(self):
        first = run_abiotic(5, ticks=4000, sample_every=100)
        second = run_abiotic(5, ticks=4000, sample_every=100)
        self.assertEqual(first, second)

    def test_control_without_replication_never_establishes(self):
        rows = [run_abiotic(seed, ticks=20000, replication=False) for seed in (1, 2)]
        for row in rows:
            self.assertFalse(row["established"])
            self.assertEqual(row["births"], 0)

    def test_detector_requires_persistence_and_mutants(self):
        samples = [
            Counter({(0, 1, 2, 3): 5, (0, 1, 2, 2): 1})
            for _ in range(LIFE_MIN_SAMPLES + 2)
        ]
        result = analyse(samples, sample_every=200)
        self.assertTrue(result["established"])
        self.assertGreaterEqual(result["max_copies"], LIFE_MIN_COPIES)
        self.assertGreaterEqual(result["mutant_neighbours"], 1)

    def test_detector_rejects_a_transient(self):
        samples = [Counter({(0, 1, 2, 3): 1}) for _ in range(3)]
        result = analyse(samples, sample_every=200)
        self.assertFalse(result["established"])

    def test_detector_rejects_an_empty_reactor(self):
        result = analyse([], sample_every=200)
        self.assertFalse(result["established"])
        self.assertEqual(result["sequences"], 0)

    def test_report_shape(self):
        row = run_abiotic(7, ticks=2000, sample_every=100)
        for key in (
            "seed", "ticks", "strands", "births", "first_strand_tick",
            "first_replication_tick", "max_copies", "persistence_ticks",
            "mutant_neighbours", "established", "evidence",
        ):
            self.assertIn(key, row)


if __name__ == "__main__":
    unittest.main()
