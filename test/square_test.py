import unittest

class TestMathFunctions(unittest.TestCase):
    
    def test_is_number_with_negative(self):
        input_value = -3
        with self.assertRaises(ValueError) as context:
            is_number(input_value)
        self.assertEqual(str(context.exception), "Input must be greater than or equal to 0")

    def test_area_with_positive_integer(self):
        input_value = 4
        expected_result = 16
        result = area(input_value)
        self.assertEqual(result, expected_result)

    def test_area_with_float(self):
        input_value = 2.5
        expected_result = 6.25
        result = area(input_value)
        self.assertAlmostEqual(result, expected_result)

    def test_area_with_negative_integer(self):
        input_value = -3
        with self.assertRaises(ValueError) as context:
            area(input_value)
        self.assertEqual(str(context.exception), "Input must be greater than or equal to 0")

    def test_area_with_invalid_string(self):
        input_value = "string"
        with self.assertRaises(ValueError) as context:
            area(input_value)
        self.assertEqual(str(context.exception), "Input must be a number")

if __name__ == "__main__":
    unittest.main()

