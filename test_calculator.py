# https://github.com/gengyuanzhang317/lab11-QZ-GZ
# Partner 1: Gengyuan Zhang
# Partner 2: Qianfan Zeng

import math
import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # ---------------- Partner 1 Responsibilities ----------------
    def test_multiply(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.multiply(3, 4), 12)
        self.assertEqual(calc.multiply(-2, 5), -10)
        self.assertEqual(calc.multiply(0, 100), 0)
        self.assertAlmostEqual(calc.multiply(2.5, 4), 10.0)

    def test_divide(self):
        calc = calculator.Calculator()
        self.assertAlmostEqual(calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(calc.divide(9, 3), 3.0)
        self.assertAlmostEqual(calc.divide(7.5, 2.5), 3.0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(3, 0)

    def test_log_invalid_argument(self):
        calc = calculator.Calculator()
        with self.assertRaises(ValueError):
            calc.log(0)
        with self.assertRaises(ValueError):
            calc.log(-5)

    def test_hypotenuse(self):
        calc = calculator.Calculator()
        self.assertAlmostEqual(calc.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calc.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(
            calc.hypotenuse(1.5, 2.0),
            math.sqrt(1.5**2 + 2.0**2)
        )

    def test_sqrt(self):
        calc = calculator.Calculator()
        self.assertAlmostEqual(calc.sqrt(9), 3.0)
        self.assertAlmostEqual(calc.sqrt(2.25), 1.5)
        with self.assertRaises(ValueError):
            calc.sqrt(-10)

    # ---------------- Partner 2 Responsibilities ----------------
    def test_add(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.add(3, 5), 8)
        self.assertEqual(calc.add(-2, 7), 5)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertAlmostEqual(calc.add(2.3, 3.7), 6.0)

    def test_subtract(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.subtract(10, 3), 7)
        self.assertEqual(calc.subtract(5, 8), -3)
        self.assertAlmostEqual(calc.subtract(2.5, 0.5), 2.0)

    def test_divide_by_zero(self):
        calc = calculator.Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)

    def test_logarithm(self):
        calc = calculator.Calculator()
        self.assertAlmostEqual(calc.logarithm(math.e), 1.0)
        self.assertAlmostEqual(calc.logarithm(100, 10), 2.0)
        self.assertAlmostEqual(calc.logarithm(8, 2), 3.0)

    def test_log_invalid_base(self):
        calc = calculator.Calculator()
        with self.assertRaises(ValueError):
            calc.logarithm(10, 1)
        with self.assertRaises(ValueError):
            calc.logarithm(10, 0)
        with self.assertRaises(ValueError):
            calc.logarithm(10, -2)


if __name__ == "__main__":
    unittest.main()