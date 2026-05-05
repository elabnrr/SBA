import unittest
from app import calculate_savings

class TestFinance(unittest.TestCase):
    def test_calculate_savings(self):
        self.assertEqual(calculate_savings(100, 50), 150)

if __name__ == '__main__':
    unittest.main()