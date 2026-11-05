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

    def test_inhabitants_can_perceive_a_conspecific(self):
        result = verify.check_conspecific_channel()
        self.assertTrue(result["passed"], result)

    def test_social_drive_rises_alone_and_eases_with_a_peer(self):
        result = verify.check_social_drive()
        self.assertTrue(result["passed"], result)

    def test_sleep_is_physiological(self):
        result = verify.check_sleep_physiology()
        self.assertTrue(result["passed"], result)

    def test_dense_shaping_pays_for_drinking(self):
        result = verify.check_shaping_attribution()
        self.assertTrue(result["passed"], result)

    def test_lives_start_at_dawn(self):
        result = verify.check_dawn_start()
        self.assertTrue(result["passed"], result)

    def test_reachability_is_measured_per_world(self):
        result = verify.check_reachability()
        self.assertTrue(result["passed"], result)


if __name__ == "__main__":
    unittest.main()
