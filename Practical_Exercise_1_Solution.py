# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# test_calculator_unittest.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
