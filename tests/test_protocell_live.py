"""Tests for the live protocell feed used by the gateway viewer."""

from __future__ import annotations

import time
import unittest

from genesis.abiotic.live import ProtocellLiveFeed


class ProtocellLiveFeedTests(unittest.TestCase):
    def test_feed_publishes_real_vesicles(self):
        feed = ProtocellLiveFeed(seed=13, warmup_ticks=800, ticks_per_second=100.0)
        feed.start()
        try:
            deadline = time.time() + 5.0
            frame = feed.snapshot()
            while time.time() < deadline and frame["population"] == 0:
                time.sleep(0.05)
                frame = feed.snapshot()
            self.assertGreater(frame["tick"], 0)
            self.assertGreater(frame["population"], 0)
            self.assertEqual(frame["mode"], "protocell")
            self.assertEqual(len(frame["cells"]), frame["population"])
            self.assertGreater(len(frame["cells"][0]), 5)
            x, y = frame["cells"][0][0], frame["cells"][0][1]
            self.assertGreaterEqual(x, 0.0)
            self.assertLessEqual(x, 16.0)
            self.assertGreaterEqual(y, 0.0)
            self.assertLessEqual(y, 16.0)
            self.assertIsNone(feed.error)
        finally:
            feed.stop()

    def test_feed_survives_stop(self):
        feed = ProtocellLiveFeed(seed=14, warmup_ticks=50, ticks_per_second=100.0)
        feed.start()
        time.sleep(0.2)
        feed.stop()
        deadline = time.time() + 5.0
        while feed._thread.is_alive() and time.time() < deadline:
            time.sleep(0.05)
        self.assertFalse(feed._thread.is_alive())


if __name__ == "__main__":
    unittest.main()
