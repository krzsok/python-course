class Frac:
    """Klasa reprezentujca uamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):
      if self.y == 1:
        return str(self.x)
      else:
        return str(self.x) + "/" + str(self.y)
      # zwraca "x/y" lub "x" dla y=1

    def __repr__(self):
      return "Frac(" + str(self.x) + ", " + str(self.y) + ")"
      # zwraca "Frac(x, y)"

    def __add__(self, other):
      mianownik = self.y * other.y
      licznik1 = other.y * self.x
      licznik2 = self.y * other.x
      return Frac(licznik1 + licznik2, mianownik)
      # frac1 + frac2

    def __sub__(self, other):
      mianownik = self.y*other.y
      licznik1 = other.y*self.x
      licznik2 = self.y*other.x
  
      return Frac(licznik1 - licznik2, mianownik)
      # frac1 - frac2

    def __mul__(self, other):
      # frac1 * frac2
      return Frac(self.x * other.x, self.y * other.y)
    
    def __div__(self, other):
      return Frac(self.x * other.y, self.y * other.x)
      # frac1 / frac2

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self * Frac(1, 1)

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):
      ulamek1 = float(self)
      ulamek2 = float(other)
  
      if ulamek1 < ulamek2:
        return -1
      elif ulamek1 > ulamek2:
        return 1
      elif ulamek1 == ulamek2:
        return 0
      # cmp(frac1, frac2)

    def __float__(self):
       return float(self.x) / float(self.y)
       # float(frac)

# Kod testujcy modu.

frac7 = Frac(2,2)
frac8 = Frac(3,2)



print frac7 + frac8
print frac7 - frac8
print frac7 * frac8
print frac8 / frac7
print + frac7
print - frac7
print ~ frac8
print cmp(frac7, frac8)
print float(frac7)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self): 
      frac7 = Frac(2,2)
      frac8 = Frac(3,2)

    def test__add__(self):
      self.assertEqual(frac7 + frac8, Frac(10,4))

    def test___sub__(self):
      self.assertEqual(frac7 - frac8, Frac(-2,4))

    def test___mul__(self):
      self.assertEqual(frac7 * frac8, Frac(6,4))

    def test___div__(self):
      self.assertEqual(frac8 / frac7 , Frac(6,4))

    def test___pos__(self): 
      self.assertEqual(+ frac7, Frac(2,2))

    def test___neg__(self):
      self.assertEqual(- frac7, Frac(-2,2))
      
    def test___invert__(self):
      self.assertEqual(~ frac8, Frac(2,3))  

    def test___cmp__(self):
      self.assertEqual(cmp(frac7, frac8), -1)

    def test___float__(self):
      self.assertEqual(float(frac7), 1.0)

    def tearDown(self): pass
      

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
