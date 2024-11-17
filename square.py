def is_number(value):
  if not isinstance(value, (int, float)):
      raise ValueError("Input must be a number")
  if value < 0:
      raise ValueError("Input must be greater than or equal to 0")

def area(a):
  '''Принимает число a, возвращает число a в квадрате'''
  is_number(a)
  return a * a

def perimeter(a):
  '''Принимает число a, возвращает 4 умноженное на a'''
  is_number(a)
  return 4 * a
