"""Tests for the live feed, the on-tick hook and the solar geometry."""

from __future__ import annotations

import math
import time
import unittest

from gateway.solar import solar_position
from genesis.soup.live import LiveFeed
from genesis.soup.pilot import run_pilot


class OnTickHookTests(unittest.TestCase):
    def test_hook_receives_frames_and_can_stop_the_run(self):
        seen = []

        def on_tick(dish, cells, ticks, births, max_gen):
            seen.append((dish.size_m, len(cells), ticks, max_gen))
            return False

        row = run_pilot(11, target_turnovers=10**9, minutes=10**9, initial=30,
                        cap=60, on_tick=on_tick)
        self.assertTrue(seen)
        self.assertGreater(seen[0][2], 0)
        self.assertEqual(row["partial"], False)
        self.assertGreater(row["ticks"], 0)

    def test_hook_that_returns_true_does_not_stop_the_run(self):
        calls = []

        def on_tick(dish, cells, ticks, births, max_gen):
            calls.append(ticks)
            return True if ticks < 6 else False

        row = run_pilot(12, target_turnovers=10**9, minutes=10**9, initial=20,
                        cap=40, on_tick=on_tick)
        self.assertGreaterEqual(row["ticks"], 6)
        self.assertEqual(len(calls), row["ticks"])


class LiveFeedTests(unittest.TestCase):
    def test_feed_publishes_real_cells(self):
        feed = LiveFeed(seed=13, initial=40, cap=80)
        feed.start()
        try:
            deadline = time.time() + 8.0
            while time.time() < deadline:
                frame = feed.snapshot()
                if frame["population"] > 0 and frame["cells"]:
                    break
                time.sleep(0.05)
            frame = feed.snapshot()
            self.assertGreater(frame["population"], 0)
            self.assertEqual(len(frame["cells"]), frame["population"])
            self.assertEqual(len(frame["nutrient"]), 256)
            self.assertAlmostEqual(frame["size_m"], 16.0)
            cell = frame["cells"][0]
            self.assertEqual(len(cell), 6)
            self.assertLessEqual(cell[0], 16.0)
            self.assertGreaterEqual(cell[0], 0.0)
        finally:
            feed.stop()

    def test_feed_survives_stop(self):
        feed = LiveFeed(seed=14, initial=20, cap=40)
        feed.start()
        time.sleep(0.5)
        feed.stop()
        deadline = time.time() + 6.0
        while feed._thread.is_alive() and time.time() < deadline:
            time.sleep(0.05)
        self.assertFalse(feed._thread.is_alive())


class SolarTests(unittest.TestCase):
    def test_equinox_noon_at_the_equator_is_near_overhead(self):
        # 2026-03-20 12:00 UTC, equator, prime meridian.
        sun = solar_position(1774008000.0, 0.0, 0.0)
        self.assertGreater(sun["elevation_deg"], 80.0)
        self.assertTrue(sun["is_day"])

    def test_midnight_at_the_equator_is_below_the_horizon(self):
        sun = solar_position(1773964800.0, 0.0, 0.0)
        self.assertLess(sun["elevation_deg"], -60.0)
        self.assertFalse(sun["is_day"])

    def test_direction_is_a_unit_vector_pointing_up_when_high(self):
        sun = solar_position(1774008000.0, 0.0, 0.0)
        length = math.sqrt(sum(value * value for value in sun["direction"]))
        self.assertAlmostEqual(length, 1.0, places=4)
        self.assertGreater(sun["direction"][1], 0.9)

    def test_polar_day_at_the_solstice(self):
        # 2026-06-21, 70 N: the sun does not set.
        sun = solar_position(1782000000.0, 70.0, 0.0)
        self.assertGreater(sun["elevation_deg"], 0.0)


if __name__ == "__main__":
    unittest.main()
