import unittest
from calculator import *
import math
import unittest
from calculator import*

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(3, 4), 12)
        self.assertEqual(calc.multiply(-2, 5), -10)
        self.assertEqual(calc.multiply(0, 100), 0)
        self.assertAlmostEqual(calc.multiply(2.5, 4), 10.0)

    def test_divide(self):
        calc = Calculator()
        self.assertAlmostEqual(calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(calc.divide(9, 3), 3.0)
        self.assertAlmostEqual(calc.divide(7.5, 2.5), 3.0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(3, 0)

    def test_log_invalid_argument(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.log(0)
        with self.assertRaises(ValueError):
            calc.log(-5)

    def test_hypotenuse(self):
        calc = Calculator()
        # c = sqrt(a^2 + b^2)
        self.assertAlmostEqual(calc.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calc.hypotenuse(5, 12), 13.0)
        # 浮点
        self.assertAlmostEqual(calc.hypotenuse(1.5, 2.0), math.sqrt(1.5**2 + 2.0**2))

    def test_sqrt(self):
        calc = Calculator()
        self.assertAlmostEqual(calc.sqrt(9), 3.0)
        self.assertAlmostEqual(calc.sqrt(2.25), 1.5)
        # invalid: sqrt(x) requires x >= 0
        with self.assertRaises(ValueError):
            calc.sqrt(-10)

if __name__ == "__main__":
    unittest.main()