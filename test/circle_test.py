import unittest
import math

class TestMathFunctions(unittest.TestCase):
    def test_is_number_with_negative(self):
        input_value = -3
        with self.assertRaises(ValueError) as context:
            is_number(input_value)
        self.assertEqual(str(context.exception), "Input must be greater than or equal to 0")

    def test_is_number_with_invalid_type(self):
        input_value = "text"
        with self.assertRaises(ValueError) as context:
            is_number(input_value)
        self.assertEqual(str(context.exception), "Input must be a number")

    def test_area_with_positive_integer(self):
        input_value = 4
        expected_result = math.pi * input_value**2
        result = area(input_value)
        self.assertAlmostEqual(result, expected_result)

    def test_area_with_float(self):
        input_value = 2.5
        expected_result = math.pi * input_value**2
        result = area(input_value)
        self.assertAlmostEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

