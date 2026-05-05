import unittest
from app import calculate_savings

class TestFinance(unittest.TestCase):
    def test_calculate_savings(self):
        self.assertEqual(calculate_savings(100, 50), 150)

    def test_negative_values(self):
        """Function should reject negative inputs."""
        with self.assertRaises(ValueError):
            calculate_savings(-100, 50)

        with self.assertRaises(ValueError):
            calculate_savings(100, -50)

if __name__ == '__main__':
    unittest.main()