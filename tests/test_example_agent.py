# Example Test for AI Agent
# Tests ensure agentic code works as expected.
import unittest
from agents.example_agent import ExampleAgent

class TestExampleAgent(unittest.TestCase):
    def test_run(self):
        agent = ExampleAgent()
        self.assertIsNone(agent.run('dummy task'))

if __name__ == '__main__':
    unittest.main()
