"""Tests for the reduced cosmogony model."""

from __future__ import annotations

import unittest

from genesis.cosmos import Cosmogony


class CosmogonyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = Cosmogony(20261105)

    def test_star_ignites(self):
        self.assertGreater(self.model.star_mass, 0.3)

    def test_planets_form(self):
        self.assertGreaterEqual(len(self.model.planets), 1)

    def test_habitable_world_is_in_the_zone_with_water(self):
        self.assertIsNotNone(self.model.focus)
        focus = self.model.focus
        self.assertGreaterEqual(focus["radius"], self.model.hz[0])
        self.assertLessEqual(focus["radius"], self.model.hz[1])
        self.assertGreaterEqual(focus["water_fraction"], 0.10)

    def test_no_planets_during_infall(self):
        early = self.model.frame(0.05)
        self.assertEqual(early["planets"], [])
        self.assertLess(early["star_mass"], 0.6)

    def test_late_frame_has_planets_and_points(self):
        late = self.model.frame(0.95)
        self.assertGreater(len(late["planets"]), 0)
        self.assertGreater(len(late["points"]), 100)

    def test_phases_appear_in_order(self):
        seen = []
        for step in range(0, 100):
            phase = self.model.phase(step / 100.0)
            if not seen or seen[-1] != phase:
                seen.append(phase)
        self.assertEqual(seen[0], "expansion")
        self.assertIn("life", seen)

    def test_deterministic_for_a_seed(self):
        other = Cosmogony(20261105)
        self.assertEqual(self.model.summary(), other.summary())

    def test_different_seeds_can_differ(self):
        other = Cosmogony(7)
        self.assertNotEqual(self.model.summary(), other.summary())


if __name__ == "__main__":
    unittest.main()
