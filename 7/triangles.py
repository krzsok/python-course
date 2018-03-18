import math
from points import Point



class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""


    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        
        
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        
        if (x1*y2+x2*y3+x2*y1) - (x1*y3+x2*y1+x3*y2) == 0:
          raise ValueError("punkty wspoliniowe")
        
        

    def __str__(self):
      return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) +  "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) +  "), (" + str(self.pt3.x) + ", " + str(self.pt3.y) +  ")]"
      # "[(x1, y1), (x2, y2), (x3, y3)]"

    def __repr__(self):
       return "Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y)  + ", " + str(self.pt3.x) + ", " + str(self.pt3.y) + ")"
      # "Triangle(x1, y1, x2, y2, x3, y3)"

    def __eq__(self, other):
      return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3 
      # obsługa tr1 == tr2

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):
      x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3.0;
      y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3.0;
      return Point(x,y)
      # zwraca środek trójkąta

    def area(self):
      a = math.sqrt((self.pt2.x - self.pt1.x)**2 + (self.pt2.y - self.pt1.y)**2 )
      b = math.sqrt((self.pt2.x - self.pt3.x)**2 + (self.pt2.y - self.pt3.y)**2 )
      c = math.sqrt((self.pt3.x - self.pt1.x)**2 + (self.pt3.y - self.pt1.y)**2 )
      
      s = a + b + c / 2.0
      
      return math.sqrt(s*(s-a)*(s-b)*(s-c))
      
      # pole powierzchni

    def move(self, x, y):
      try:
        val = int(x)
        val = int(y)
      except ValueError:
        raise ValueError("That's not an int!")
      self.pt1.x += x
      self.pt2.x += x
      self.pt3.x += x
      
      self.pt1.y += y
      self.pt2.y += y
      self.pt3.y += y
      
      # przesunięcie o (x, y)

    def make4(self):
      q1 = (self.pt1.x + self.pt2.x) /2.0
      q2 = (self.pt1.y + self.pt2.y) /2.0
      w1 = (self.pt2.x + self.pt3.x) /2.0
      w2 = (self.pt3.y + self.pt3.y) /2.0
      e1 = (self.pt1.x + self.pt3.x) /2.0
      e2 = (self.pt1.y + self.pt3.y) /2.0
      
      return [Triangle(self.pt1.x,self.pt1.y, q1, q2, e1, e2), Triangle(q1, q2, e1, e2, w1, w2), Triangle(q1,q2,self.pt2.x,self.pt2.y,w1,w2), Triangle(self.pt3.x,self.pt3.y,e1,e2,w1,w2)]
      
      # zwraca listę czterech mniejszych

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):

  
  def setUp(self):
    self.triangle1 = Triangle(1,1,2,1,1,3)
    self.triangle2 = Triangle(2,1,4,1,1,3)
    self.triangle3 = Triangle(3,2,5,2,2,4)
    
  def test_area(self):
    self.assertEqual(self.triangle1.area(), 7.8297478685457715 )
    

  def test_move(self):
    self.triangle2.move(1,1)
    self.assertEqual(self.triangle2 == self.triangle3, True )
    
  def test_center(self):
    self.assertEqual(self.triangle1.center(), Point(1.3333333333333333, 1.6666666666666667))

   
  def tearDown(self): pass
      

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

