import json
import os
import random
import tempfile
import unittest

from genesis.soup.dish import NutrientDish
from genesis.soup.genome import GENES, Genome
from genesis.soup.pilot import Cell, _snapshot, evaluate, format_table, run_pilot


class SoupGenome(unittest.TestCase):
    def test_mutation_stays_inside_declared_ranges(self):
        rng = random.Random(7)
        genome = Genome.founding(rng)
        for _ in range(400):
            genome = genome.mutate(rng)
            for value, (_, low, high, _) in zip(genome.values, GENES):
                self.assertGreaterEqual(value, low)
                self.assertLessEqual(value, high)

    def test_distance_is_bounded_and_symmetric(self):
        rng = random.Random(9)
        a = Genome.founding(rng)
        b = Genome.founding(rng)
        self.assertAlmostEqual(a.distance(b), b.distance(a), places=12)
        self.assertEqual(a.distance(a), 0.0)


class SoupDish(unittest.TestCase):
    def test_diffusion_conserves_nutrient(self):
        # Regrowth adds nutrient by design, so isolate diffusion for the ledger.
        dish = NutrientDish(regrow=0.0)
        before = dish.total()
        for _ in range(25):
            dish.step()
        self.assertAlmostEqual(dish.total(), before, places=6)

    def test_dish_is_bounded_and_depletable(self):
        dish = NutrientDish()
        self.assertEqual(dish.patch_at(-5.0, 99.0), dish.patch_mask[-1])
        taken = dish.take(4.0, 4.0, 10.0)
        self.assertGreater(taken, 0.0)
        self.assertEqual(dish.at(4.0, 4.0), 0.0)

    def test_regrowth_is_capped(self):
        dish = NutrientDish()
        for _ in range(400):
            dish.step()
        self.assertLessEqual(max(dish.values), dish.cap + 1e-12)


class SoupPilot(unittest.TestCase):
    def _run(self, seed, turnovers=2):
        # A generous cap and a short wall clock: capping the population would stall
        # births and make the test sit out its time limit.
        return run_pilot(
            seed, target_turnovers=turnovers, minutes=0.05, initial=30, cap=300
        )

    def test_short_run_produces_cells_and_metrics(self):
        row = self._run(20261105)
        self.assertGreater(row["turnovers"], 0.0)
        self.assertGreater(row["final"]["population"], 0)
        self.assertGreater(row["ticks"], 0)
        for key in ("median_depth", "diversity", "niche_entropy", "traits", "turnovers"):
            self.assertIn(key, row["final"])
        self.assertIn("ticks_per_s", row)

    def test_same_seed_is_deterministic(self):
        a = self._run(11)
        b = self._run(11)
        self.assertEqual(a["digest"], b["digest"])
        self.assertEqual(a["ticks"], b["ticks"])

    def test_checkpoint_is_written_during_the_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "seed.partial.json")
            row = run_pilot(
                5, target_turnovers=6, minutes=0.05, initial=30, cap=300,
                checkpoint_path=path, checkpoint_every=1,
            )
            with open(path, encoding="utf-8") as handle:
                payload = json.load(handle)
        self.assertTrue(payload["partial"])
        self.assertEqual(payload["rows"][0]["seed"], 5)
        self.assertLessEqual(payload["rows"][0]["turnovers"], row["turnovers"])
        self.assertFalse(os.path.exists(path + ".tmp"))
        self.assertFalse(row["partial"])

    def test_reports_floor_and_per_lineage_breakdown(self):
        row = self._run(21)
        self.assertEqual(row["floor_turnovers"], 1000)
        self.assertEqual(row["clock"], "turnovers (births / mean population)")
        self.assertIn("lineages", row["final"])
        self.assertIn("top_lineages", row["final"])
        self.assertIn("births", row["final"])

    def test_niche_entropy_is_median_across_lineages(self):
        # One lineage fed from a single patch (entropy 0), one fed equally from all
        # three (entropy 1). Median across lineages is the upper median, 1.0.
        rng = random.Random(1)
        cells = [
            Cell(1.0, 1.0, 0.0, 1.0, Genome.founding(rng), 5, 1) for _ in range(3)
        ]
        cells.append(Cell(1.0, 1.0, 0.0, 1.0, Genome.founding(rng), 5, 2))
        snapshot = _snapshot(cells, {1: {0: 1.0}, 2: {0: 1.0, 1: 1.0, 2: 1.0}}, 10)
        self.assertEqual(snapshot["niche_entropy"], 1.0)
        self.assertEqual(snapshot["niche_breadth"], 3.0)
        self.assertEqual(snapshot["lineages"], 2)

    def test_table_formats(self):
        row = self._run(3)
        text = format_table([row])
        self.assertIn("seed", text)
        self.assertIn("turn", text)
        self.assertIn(str(row["seed"]), text)


class SoupFalsifier(unittest.TestCase):
    def _row(self, seed, depth=500, base_entropy=1.0, final_entropy=0.4,
             base_traits=None, final_traits=None, reached=True, extinct=False):
        base_traits = base_traits or {"speed": 0.1, "size": 1.0}
        final_traits = final_traits or base_traits
        return {
            "seed": seed,
            "reached_target": reached,
            "extinct_after_floor": extinct,
            "baseline": {"niche_entropy": base_entropy, "traits": base_traits},
            "final": {
                "median_depth": depth,
                "niche_entropy": final_entropy,
                "traits": final_traits,
            },
        }

    def test_pass_needs_all_four(self):
        rows = [self._row(seed) for seed in range(5)]
        rows = [
            self._row(
                row["seed"],
                base_traits={"speed": 0.1, "size": 1.0},
                final_traits={"speed": 0.4, "size": 1.0},
            )
            for row in rows
        ]
        verdict = evaluate(rows)
        self.assertTrue(verdict["passed"], verdict)
        self.assertLess(verdict["checks"]["trait_selection_ge_2sd"]["z"], 100.0)

    def test_extinction_after_floor_fails(self):
        rows = [self._row(seed) for seed in range(4)]
        rows.append(self._row(4, extinct=True))
        verdict = evaluate(rows)
        self.assertFalse(verdict["passed"])
        self.assertFalse(verdict["checks"]["survived_after_floor"])

    def test_flat_entropy_fails(self):
        rows = [self._row(seed, final_entropy=1.0) for seed in range(5)]
        verdict = evaluate(rows)
        self.assertFalse(verdict["checks"]["entropy_halved"]["passed"])
        self.assertFalse(verdict["passed"])

    def test_zero_baseline_entropy_cannot_pass(self):
        # If the gen-100 median is already at the floor, halving is impossible and the
        # criterion must fail loudly rather than divide by zero.
        rows = [self._row(seed, base_entropy=0.0, final_entropy=0.0) for seed in range(5)]
        verdict = evaluate(rows)
        self.assertFalse(verdict["checks"]["entropy_halved"]["passed"])
        self.assertIsNone(verdict["checks"]["entropy_halved"]["median_ratio"])
        self.assertFalse(verdict["passed"])


if __name__ == "__main__":
    unittest.main()
