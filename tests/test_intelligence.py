import unittest

from genesis import verify


class IntelligenceValidation(unittest.TestCase):
    def test_prediction_error_decreases_with_experience(self):
        result = verify.check_prediction_learning()
        self.assertTrue(result["passed"], result)

    def test_both_architectures_are_comparable(self):
        result = verify.check_brain_parity()
        self.assertTrue(result["passed"], result)

    def test_only_two_permitted_architectures(self):
        result = verify.check_only_two_architectures()
        self.assertTrue(result["passed"], result)

    def test_sensory_firewall_blocks_omniscience(self):
        result = verify.check_sensory_firewall()
        self.assertTrue(result["passed"], result)

    def test_death_is_permanent_and_recorded(self):
        result = verify.check_death_permanence()
        self.assertTrue(result["passed"], result)

    def test_knowledge_transfers_between_inhabitants(self):
        result = verify.check_knowledge_transfer()
        self.assertTrue(result["passed"], result)


if __name__ == "__main__":
    unittest.main()
