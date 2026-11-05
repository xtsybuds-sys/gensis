import os
import tempfile
import unittest

from genesis import verify
from genesis.config import Config
from genesis.sim import Simulation
from genesis.store import Store


class IntegrationValidation(unittest.TestCase):
    def test_same_seed_produces_identical_world(self):
        result = verify.check_determinism()
        self.assertTrue(result["passed"], result)

    def test_checkpoint_resume_is_bit_identical(self):
        result = verify.check_checkpoint_resume()
        self.assertTrue(result["passed"], result)

    def test_five_inhabitants_get_separate_houses(self):
        result = verify.check_population_setup()
        self.assertTrue(result["passed"], result)

    def test_short_run_produces_metrics_and_logs(self):
        cfg = Config(days=0.02, grid=12, population=5, checkpoint_every=0,
                     log_every=180)
        sim = Simulation(cfg)
        for _ in range(900):
            sim.step()
        self.assertEqual(sim.tick, 900)
        self.assertGreater(len(sim.metrics_history), 0)
        snapshot = sim.snapshot()
        for key in ("alive", "encounters", "discoveries", "water_m3", "clock"):
            self.assertIn(key, snapshot)
        # Five start; one-mind means every inhabitant is hybrid, so a birth can
        # legitimately add to the population inside the run.
        self.assertGreaterEqual(snapshot["population"], 5)

    def test_store_persists_events_and_checkpoints(self):
        directory = tempfile.mkdtemp()
        path = os.path.join(directory, "run.sqlite")
        store = Store(path)
        cfg = Config(days=0.01, grid=10, population=2, checkpoint_every=0,
                     log_every=0)
        sim = Simulation(cfg, store)
        for _ in range(40):
            sim.step()
        sim.checkpoint()
        counts = store.counts()
        self.assertGreaterEqual(counts["events"], 2)
        self.assertEqual(counts["checkpoints"], 1)
        self.assertIsNotNone(store.latest_checkpoint())
        store.close()


if __name__ == "__main__":
    unittest.main()
