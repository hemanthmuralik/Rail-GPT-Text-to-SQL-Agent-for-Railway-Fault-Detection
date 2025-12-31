import unittest
from agent import is_safe_input

class TestRailGPT(unittest.TestCase):

    def setUp(self):
        print("\n----------------------------------------------------------------------")

    # --- TEST SUITE 1: MALICIOUS INPUTS (The Guardrails) ---
    def test_prevention_of_destructive_commands(self):
        """Ensure all destructive SQL commands are blocked."""
        malicious_prompts = [
            "DROP TABLE faults",
            "DELETE FROM faults WHERE id > 0",
            "TRUNCATE TABLE faults",
            "UPDATE faults SET status = 'Fixed'",
            "INSERT INTO faults VALUES (1, 'Fake', '2025-01-01', 'Test', 0.9, 'New')"
        ]
        
        print(f"🛡️  Testing {len(malicious_prompts)} Malicious Inputs...")
        for prompt in malicious_prompts:
            is_safe, msg = is_safe_input(prompt)
            self.assertFalse(is_safe, f"Failed to block: {prompt}")
            print(f"   ✅ Blocked: '{prompt}'")

    # --- TEST SUITE 2: VALID INPUTS (The Logic) ---
    def test_allowance_of_valid_queries(self):
        """Ensure legitimate questions pass the filter."""
        valid_prompts = [
            "How many cracks were detected in Pune?",
            "Show me the top 5 faults by confidence score.",
            "List all pending issues from yesterday.",
            "What is the average confidence score?",
            "Select the location with the most errors."
        ]

        print(f"✅ Testing {len(valid_prompts)} Valid Inputs...")
        for prompt in valid_prompts:
            is_safe, msg = is_safe_input(prompt)
            self.assertTrue(is_safe, f"Wrongly blocked safe query: {prompt}")
            print(f"   ok Allowed: '{prompt}'")

if __name__ == '__main__':
    print("🚀 Starting Rail-GPT Automated Security Suite")
    unittest.main()
