import unittest

from genesis import verify


class PhysicsValidation(unittest.TestCase):
    def test_water_mass_conservation(self):
        result = verify.check_water_mass_conservation()
        self.assertTrue(result["passed"], result)

    def test_shallow_water_dynamics(self):
        result = verify.check_shallow_water_dynamics()
        self.assertTrue(result["passed"], result)

    def test_thermal_diffusion_conservation(self):
        result = verify.check_thermal_diffusion_conservation()
        self.assertTrue(result["passed"], result)

    def test_thermal_energy_ledger(self):
        result = verify.check_thermal_ledger()
        self.assertTrue(result["passed"], result)

    def test_free_fall_matches_analytic_solution(self):
        result = verify.check_free_fall_accuracy()
        self.assertTrue(result["passed"], result)

    def test_ballistic_energy_drift_is_negligible(self):
        result = verify.check_ballistic_energy_drift()
        self.assertTrue(result["passed"], result)

    def test_restitution_apex_matches_coefficient(self):
        result = verify.check_restitution()
        self.assertTrue(result["passed"], result)


if __name__ == "__main__":
    unittest.main()
