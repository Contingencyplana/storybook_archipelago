# ✅ integtest.py
# Tests the routing logic in integration.py

import unittest
from . import integration

class TestIntegrationRouting(unittest.TestCase):

    def setUp(self):
        self.memory = {}

    def test_left_input(self):
        output = integration.route_input("L", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("left", output.lower())

    def test_right_input(self):
        output = integration.route_input("R", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("right", output.lower())

    def test_invalid_input_triggers_story(self):
        output = integration.route_input("?", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("grove", output.lower())  # Expect poetic scene

    def test_case_insensitivity(self):
        output = integration.route_input("l", self.memory)
        self.assertIsInstance(output, str)
        self.assertIn("left", output.lower())

if __name__ == "__main__":
    unittest.main()
