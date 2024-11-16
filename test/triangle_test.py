import unittest
import math

class TestTriangleFunctions(unittest.TestCase):
    def test_area_with_float_triangle(self):
        a, b, c = 2.5, 4.5, 5.5
        p = (a + b + c) / 2
        expected_result = math.sqrt(p * (p - a) * (p - b) * (p - c))
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_result)

    def test_area_with_negative_side(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError) as context:
            area(a, b, c)
        self.assertEqual(str(context.exception), "Input must be greater than or equal to 0")

    def test_area_with_invalid_type(self):
        a, b, c = 3, "side", 5
        with self.assertRaises(ValueError) as context:
            area(a, b, c)
        self.assertEqual(str(context.exception), "Input must be a number")

    def test_perimeter_with_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_result = 12
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_result)

    def test_perimeter_with_floats(self):
        a, b, c = 2.5, 4.5, 5.5
        expected_result = a + b + c
        result = perimeter(a, b, c)
        self.assertAlmostEqual(result, expected_result)

    def test_perimeter_with_negative_side(self):
        a, b, c = 3, -4, 5
        with self.assertRaises(ValueError) as context:
            perimeter(a, b, c)
        self.assertEqual(str(context.exception), "Input must be greater than or equal to 0")

    def test_perimeter_with_invalid_type(self):
        a, b, c = 3, "side", 5
        with self.assertRaises(ValueError) as context:
            perimeter(a, b, c)
        self.assertEqual(str(context.exception), "Input must be a number")

if __name__ == "__main__":
    unittest.main()

