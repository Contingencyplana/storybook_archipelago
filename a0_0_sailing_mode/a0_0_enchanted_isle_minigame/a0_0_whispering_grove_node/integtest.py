# ✅ integtest.py
# Tests the routing logic in integration.py
import unittest
import a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_0_whispering_grove_node.integration as integration

class TestIntegrationRouting(unittest.TestCase):
    def setUp(self):
        self.memory = {}

    def test_left_input(self):
        output = integration.route_input("L", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("[LEFT]", output)

    def test_right_input(self):
        output = integration.route_input("R", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("[RIGHT]", output)

    def test_invalid_input_triggers_story(self):
        output = integration.route_input("Z", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("grove", output.lower())
        self.assertNotIn("[PORTAL:", output)

    def test_case_insensitivity(self):
        output = integration.route_input("l", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("[LEFT]", output)

if __name__ == "__main__":
    unittest.main()
