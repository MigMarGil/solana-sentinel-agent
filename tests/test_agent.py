import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ai_agent import SecurityAgent

class TestSecurityAgent(unittest.TestCase):
    def setUp(self):
        self.agent = SecurityAgent()

    def test_safe_simulation(self):
        safe_sim = {
            "result": {
                "value": {
                    "err": None,
                    "logs": [
                        "Program 11111111111111111111111111111111 invoke [1]",
                        "Program 11111111111111111111111111111111 success"
                    ],
                    "unitsConsumed": 150
                }
            }
        }
        report = self.agent.analyze_simulation(safe_sim)
        self.assertEqual(report["severity"], "LOW")
        self.assertEqual(report["risk_score"], 0)

    def test_malicious_simulation(self):
        malicious_sim = {
            "result": {
                "value": {
                    "err": None,
                    "logs": [
                        "Program BadDrainer111111111111111111111111111111 invoke [1]",
                        "Program BadDrainer111111111111111111111111111111 failed: custom program error: 0x1"
                    ],
                    "unitsConsumed": 185000
                }
            }
        }
        report = self.agent.analyze_simulation(malicious_sim)
        self.assertIn(report["severity"], ["MEDIUM", "CRITICAL"])
        self.assertTrue(len(report["risk_factors"]) > 0)

if __name__ == "__main__":
    unittest.main()
