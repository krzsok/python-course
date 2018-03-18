import math
from points import Point

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
      return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) +  ", " + str(self.radius) + ")"
      # "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
      return self.radius * self.radius * math.pi
      # pole powierzchni

    def move(self, x, y):
      try:
        val = int(x)
        val = int(y)
      except ValueError:
        raise ValueError("That's not an int!")
      self.pt.x += x
      self.pt.y += y
      # przesuniecie o (x, y)

    def cover(self, other):
      x = (self.pt.x + other.pt.x) / 2.0 
      y = (self.pt.y + other.pt.y) / 2.0
      
      radius = math.sqrt((other.pt.x - self.pt.x)**2 + (other.pt.y - self.pt.y)**2 ) + max(self.radius, other.radius) 
      return Circle(x, y, radius)
      # okrąg pokrywający oba

# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):
  
  def setUp(self):
    self.circle1 = Circle(2,3,5)
    self.circle2 = Circle(4,6,4)
    self.circle3 = Circle(1,1,1)

  def test_area(self):
    self.assertEqual(self.circle1.area(), 78.53981633974483 )
    

  def test_move(self):
    self.circle3.move(1,1)
    self.assertEqual(self.circle3.pt.x, 2 )
    self.assertEqual(self.circle3.pt.y, 2 )
    
  def test_cover(self):
    self.assertEqual(self.circle1.cover(self.circle2), Circle(3.0, 4.5, 8.60555127546399) )

   
  def tearDown(self): pass
      

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy


