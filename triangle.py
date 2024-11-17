import math

def is_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    if value < 0:
        raise ValueError("Input must be greater than or equal to 0")

def area(a, b, c):
    '''Возвращает площадь треугольника по формуле Герона'''
    is_number(a)
    is_number(b)
    is_number(c)
    p = (a + b + c) / 2
    area_squared = p * (p - a) * (p - b) * (p - c)
    if area_squared <= 0:
        raise ValueError("The provided sides do not form a valid triangle.")
    return math.sqrt(area_squared)

def perimeter(a, b, c):
    '''Возвращает периметр треугольника'''
    is_number(a)
    is_number(b)
    is_number(c)
    return a + b + c
