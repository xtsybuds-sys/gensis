import unittest

from genesis.soup.dish import NutrientDish
from genesis.soup.genome import GENES, Genome
from genesis.soup.pilot import Cell, _snapshot, evaluate, format_table, run_pilot
from genesis.util import stable_hash
import random


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
    def _run(self, seed, generations=2):
        # A generous cap and a short wall clock: capping the population would stall
        # lineage depth and make the test sit out its time limit.
        return run_pilot(
            seed, generations=generations, minutes=0.05, initial=30, cap=300
        )

    def test_short_run_produces_cells_and_metrics(self):
        row = self._run(20261105)
        self.assertGreaterEqual(row["max_gen"], 1)
        self.assertGreater(row["final"]["population"], 0)
        self.assertGreater(row["ticks"], 0)
        for key in ("median_depth", "diversity", "niche_breadth", "traits"):
            self.assertIn(key, row["final"])
        self.assertIn("ticks_per_s", row)

    def test_same_seed_is_deterministic(self):
        a = self._run(11)
        b = self._run(11)
        self.assertEqual(a["digest"], b["digest"])
        self.assertEqual(a["ticks"], b["ticks"])

    def test_reports_floor_and_per_lineage_breakdown(self):
        row = self._run(21)
        self.assertEqual(row["floor_generations"], 1000)
        self.assertIn("lineages", row["final"])
        self.assertIn("top_lineages", row["final"])

    def test_niche_breadth_is_median_across_lineages(self):
        # Three cells of one lineage that found one patch, one cell of another that
        # found all three. Median across lineages is 3, not the population-weighted 1.
        rng = random.Random(1)
        cells = [
            Cell(1.0, 1.0, 0.0, 1.0, Genome.founding(rng), 5, 1) for _ in range(3)
        ]
        cells.append(Cell(1.0, 1.0, 0.0, 1.0, Genome.founding(rng), 5, 2))
        snapshot = _snapshot(cells, {1: {0}, 2: {0, 1, 2}}, 10)
        self.assertEqual(snapshot["niche_breadth"], 3.0)
        self.assertEqual(snapshot["lineages"], 2)
        self.assertEqual(len(snapshot["top_lineages"]), 2)

    def test_table_formats(self):
        row = self._run(3)
        text = format_table([row])
        self.assertIn("seed", text)
        self.assertIn(str(row["seed"]), text)


class SoupFalsifier(unittest.TestCase):
    def _row(self, seed, depth, niche, base, traits, reached=True, extinct=False,
             final_traits=None):
        return {
            "seed": seed,
            "reached_target": reached,
            "extinct_after_floor": extinct,
            "baseline": {"niche_breadth": base, "traits": traits},
            "final": {
                "median_depth": depth,
                "niche_breadth": niche,
                "traits": final_traits or traits,
            },
        }

    def test_pass_needs_all_four(self):
        traits = {"speed": 0.1, "size": 1.0}
        shifted = {"speed": 0.4, "size": 1.0}
        rows = [
            self._row(seed, 500, 3, 1, traits, final_traits=shifted)
            for seed in range(5)
        ]
        verdict = evaluate(rows)
        self.assertTrue(verdict["passed"], verdict)

    def test_extinction_after_floor_fails(self):
        traits = {"speed": 0.1, "size": 1.0}
        rows = [self._row(seed, 500, 3, 1, traits) for seed in range(4)]
        rows.append(self._row(4, 500, 3, 1, traits, extinct=True))
        verdict = evaluate(rows)
        self.assertFalse(verdict["passed"])
        self.assertFalse(verdict["checks"]["survived_last_10k"])

    def test_flat_niche_fails(self):
        traits = {"speed": 0.1, "size": 1.0}
        rows = [self._row(seed, 500, 2, 2, traits) for seed in range(5)]
        verdict = evaluate(rows)
        self.assertFalse(verdict["checks"]["niche_breadth_doubled"]["passed"])
        self.assertFalse(verdict["passed"])


if __name__ == "__main__":
    unittest.main()
