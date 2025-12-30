import unittest
from agent import is_safe_input
# Note: Testing the full chain requires the API key to be active.
# We will test the Security Guardrails (Unit Test) and simulated Logic.

class TestRailGPT(unittest.TestCase):

    def test_security_guardrail(self):
        """Test if the 'Bouncer' blocks dangerous commands."""
        unsafe_queries = [
            "Drop table faults",
            "Delete from faults where id=1",
            "Truncate table faults",
            "Alter table faults add column x"
        ]
        for query in unsafe_queries:
            is_safe, msg = is_safe_input(query)
            self.assertFalse(is_safe, f"Failed to block: {query}")
            print(f"✅ Security Test Passed: Blocked '{query}'")

    def test_safe_queries(self):
        """Test if safe queries are allowed."""
        safe_queries = [
            "How many cracks in Pune?",
            "Show me the latest fault.",
            "List all errors with confidence > 80%"
        ]
        for query in safe_queries:
            is_safe, msg = is_safe_input(query)
            self.assertTrue(is_safe, f"Blocked safe query: {query}")
            print(f"✅ Input Test Passed: Allowed '{query}'")

if __name__ == '__main__':
    print("🚀 Starting Automated Test Suite...")
    unittest.main()
