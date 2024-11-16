import math

def is_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    if value < 0:
        raise ValueError("Input must be greater than or equal to 0")

def area(a, b, c):
    '''Принимает число a, b, c, возвращает половину сумму a, b, c'''
    is_number(a)
    is_number(b)
    is_number(c)
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


def perimeter(a, b, c):
    '''Принимает число a, b, c, возвращает сумму a, b, c'''
    is_number(a)
    is_number(b)
    is_number(c)
    return a + b + c
