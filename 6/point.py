import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x=0, y=0):  # konstuktor
      self.x = x
      self.y = y

    def __str__(self):
      return "(" + str(self.x) + ", " + str(self.y) + ")"
      # zwraca string "(x, y)"

    def __repr__(self):
      return "Point(" + str(self.x) + ", " + str(self.y) + ")"
      # zwraca string "Point(x, y)"

    def __eq__(self, other):
      if self.x == other.x and self.y == other.y:
        return True
      else:
        return False
      # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
      return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
      return Point(self.x + other.x, self.y + other.y)
      # v1 + v2

    def __sub__(self, other):
      return Point(self.x - other.x, self.y - other.y)
      # v1 - v2

    def __mul__(self, other):
      return self.x * other.x + self.y * other.y
      # v1 * v2, iloczyn skalarny

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
      return self.x * other.y - self.y * other.x

    def length(self):
      return math.sqrt(self.x * self.x + self.y * self.y)
      # długość wektora

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    
    def setUp(self):
      self.point1 = Point(2,4)
      self.point2 = Point(1,3)


    def test__add__(self):
      self.assertEqual(self.point1 + self.point2, Point(3,7))

    def test___sub__(self):
      self.assertEqual(self.point1 - self.point2, Point(1,1))

    def test___mul__(self):
      self.assertEqual(self.point1 * self.point2, 14)

    def test_cross(self):
      self.assertEqual(self.point1.cross(self.point2) , 2)

    def test_length(self): 
      self.assertEqual(self.point1.length(), 4.47213595499958 )

   
    def tearDown(self): pass
      

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

