import math

def is_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    if value < 0:
        raise ValueError("Input must be greater than or equal to 0")

def area(r):
    is_number(r)
    return math.pi * r * r

def perimeter(r):
    is_number(r)
    return 2 * math.pi * r
