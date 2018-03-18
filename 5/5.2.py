def add_frac(frac1, frac2):
  mianownik = frac1[1]*frac2[1]
  licznik1 = frac2[1]*frac1[0]
  licznik2 = frac1[1]*frac2[0]
    
  return [licznik1 + licznik2, mianownik]
  # frac1 + frac2

def sub_frac(frac1, frac2):
  mianownik = frac1[1]*frac2[1]
  licznik1 = frac2[1]*frac1[0]
  licznik2 = frac1[1]*frac2[0]
  
  return [licznik1 - licznik2, mianownik]
  # frac1 - frac2

def mul_frac(frac1, frac2):
  return [frac1[0] * frac2[0], frac1[1] * frac2[1]]
  # frac1 * frac2

def div_frac(frac1, frac2):
  return [frac1[0] * frac2[1], frac1[1] * frac2[0]]
  # frac1 / frac2

def is_positive(frac):
  if frac[0] > 0 and frac[1] > 0:
    return True
  else:
    return False
  # bool, czy dodatni

def is_zero(frac):
  if frac[0] == 0:
    return True
  else:
    return False
  # bool, typu [0, x]

def cmp_frac(frac1, frac2):
  ulamek1 = frac2float(frac1)
  ulamek2 = frac2float(frac2)
  
  if ulamek1 < ulamek2:
    return -1
  elif ulamek1 > ulamek2:
    return 1
  elif ulamek1 == ulamek2:
    return 0
  
  # -1 | 0 | +1 -1 jesli frac1 mniejszy, 0 jesli rowne, +1 jesli frac1 wiekszy

def frac2float(frac):
  return float(frac[0]) / float(frac[1])
  # konwersja do float

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
      self.zero = [0, 1]

    def test_add_frac(self):
      self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
      self.assertEqual(sub_frac([-1, 2], [3, 1]), [-7, 2])

    def test_mul_frac(self):
      self.assertEqual(mul_frac([-1, 2], [3, 1]), [-3, 2])

    def test_div_frac(self):
      self.assertEqual(div_frac([-1, 2], [3, 1]), [-1, 6])

    def test_is_positive(self): 
      self.assertEqual(is_positive([-1, 2]), False)

    def test_is_zero(self): 
      self.assertEqual(is_zero([-1, 2]), False)

    def test_cmp_frac(self): 
      self.assertEqual(cmp_frac([-1, 2], [1, 3]), -1)

    def test_frac2float(self): 
      self.assertEqual(frac2float([-1, 2]), -0.5)

    def tearDown(self): pass
      

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
