import random
import unittest

from genesis.brains import BRAIN_KINDS, make_brain
from genesis.brains.baseline import RandomPolicy
from genesis.config import Config
from genesis.experiments import run_variant
from genesis.genetics import HIDDEN_CHOICES, Genome
from genesis.sim import Simulation


class GenomeTests(unittest.TestCase):
    def test_mutation_stays_within_bounds(self):
        rng = random.Random(1)
        genome = Genome.random(rng, "neural")
        for _ in range(300):
            genome = genome.mutate(rng)
            self.assertIn(genome.hidden, HIDDEN_CHOICES)
            self.assertTrue(0.004 <= genome.plasticity <= 0.06)
            self.assertTrue(0.0 <= genome.novelty_weight <= 0.9)
            self.assertTrue(0.15 <= genome.w_scale <= 0.9)

    def test_genome_round_trips_through_dict(self):
        genome = Genome(
            brain_kind="hybrid",
            hidden=16,
            plasticity=0.03,
            novelty_weight=0.5,
            w_scale=0.6,
        )
        self.assertEqual(Genome.from_dict(genome.to_dict()), genome)

    def test_brain_is_built_from_genome(self):
        genome = Genome(
            brain_kind="neural",
            hidden=16,
            plasticity=0.031,
            novelty_weight=0.5,
            w_scale=0.6,
        )
        brain = make_brain("neural", random.Random(2), Config(), genome=genome)
        self.assertEqual(brain.hidden, 16)
        self.assertAlmostEqual(brain.plasticity, 0.031)


class ReproductionTests(unittest.TestCase):
    def _ready_sim(self, **kwargs):
        cfg = Config(
            days=0.01,
            grid=10,
            population=2,
            log_every=0,
            checkpoint_every=0,
            reproduction_cooldown_s=0.0,
            **kwargs,
        )
        sim = Simulation(cfg)
        first, second = sim.agents[0], sim.agents[1]
        second.pos = [first.pos[0] + 2.0, first.pos[1]]
        for agent in (first, second):
            agent.energy = 1.0
            agent.nutrition = 1.0
            agent.hydration = 1.0
            agent.cooldown_s = 0.0
            agent.sleeping = False
        return sim

    def test_reproduction_creates_generation_one(self):
        sim = self._ready_sim()
        parent_a, parent_b = sim.agents[0], sim.agents[1]
        child = sim._reproduce(sim.tick)
        self.assertIsNotNone(child)
        self.assertEqual(child.generation, 1)
        self.assertEqual(len(sim.agents), 3)
        self.assertEqual(sim.births, 1)
        self.assertEqual(parent_a.children, 1)
        self.assertEqual(child.parents, [parent_a.aid, parent_b.aid])
        self.assertEqual(child.genome.brain_kind, parent_a.genome.brain_kind)

    def test_population_cap_blocks_births(self):
        sim = self._ready_sim(max_population=2)
        self.assertIsNone(sim._reproduce(sim.tick))
        self.assertEqual(sim.births, 0)

    def test_reproduction_requires_proximity(self):
        sim = self._ready_sim(reproduction_range_m=1.0)
        sim.agents[1].pos = [sim.agents[0].pos[0] + 50.0, sim.agents[0].pos[1]]
        self.assertIsNone(sim._reproduce(sim.tick))

    def test_exhausted_parent_cannot_reproduce(self):
        sim = self._ready_sim()
        sim.agents[0].energy = 0.1
        self.assertIsNone(sim._reproduce(sim.tick))


class DreamModeTests(unittest.TestCase):
    def test_sleeping_inhabitants_skip_decisions(self):
        cfg = Config(
            days=0.01,
            grid=10,
            population=1,
            log_every=0,
            checkpoint_every=0,
            dream_every=6,
        )
        sim = Simulation(cfg)
        agent = sim.agents[0]
        agent.energy = 0.5
        agent.sleeping = True
        for _ in range(40):
            sim.step()
        self.assertTrue(agent.sleeping)
        self.assertGreater(sim.skipped_decisions, 0)
        self.assertEqual(sim.decisions, 0)

    def test_awake_inhabitants_do_decide(self):
        cfg = Config(
            days=0.01, grid=10, population=1, log_every=0, checkpoint_every=0
        )
        sim = Simulation(cfg)
        for _ in range(40):
            sim.step()
        # The world clock starts at night, so some ticks may legitimately be
        # skipped for sleep; the point is that awake decision ticks happen.
        self.assertGreater(sim.decisions, 0)


class AblationTests(unittest.TestCase):
    def test_planner_can_be_disabled(self):
        off = make_brain("hybrid", random.Random(2), Config(planner=False))
        on = make_brain("hybrid", random.Random(2), Config(planner=True))
        self.assertFalse(off.planner_enabled)
        self.assertTrue(on.planner_enabled)

    def test_random_baseline_is_not_an_inhabitant_architecture(self):
        self.assertEqual(BRAIN_KINDS, ("neural", "hybrid"))
        brain = RandomPolicy(random.Random(3))
        output = brain.act([0.0] * 24)
        self.assertEqual(len(output), 6)
        self.assertTrue(all(-1.0 <= value <= 1.0 for value in output))
        self.assertEqual(brain.stats()["kind"], "baseline-random")


class CalibrationHarnessTests(unittest.TestCase):
    def test_variant_reports_calibration_fields(self):
        result = run_variant(
            seed=7, days=0.05, arm="population", grid=10, population=3
        )
        for key in (
            "survivors",
            "observed_days",
            "first_drink_day",
            "births",
            "sleep_skipped_fraction",
            "ticks_per_s",
        ):
            self.assertIn(key, result)
        self.assertEqual(result["ticks"], 432)

    def test_random_arm_uses_baseline_policy(self):
        result = run_variant(
            seed=7, days=0.03, arm="random", grid=10, population=2
        )
        self.assertEqual(result["arm"], "random")
        self.assertGreater(result["ticks"], 0)
        self.assertLessEqual(result["survivors"], result["population_end"])


if __name__ == "__main__":
    unittest.main()
