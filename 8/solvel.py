def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 :
      print "brak rozwiazan"
    elif a == 0 :
      print "rozwiazania klasy (r , -(c/b)), gdzie r nalezy do liczb rzeczywistych, a c i b to odpowiednio " + str(c) + ", " + str(b) 
    elif b == 0 :
      print "rozwiazania klasy (-(c/a), r), gdzie r nalezy do liczb rzeczywistych, a c i a to odpowiednio " + str(c) + ", " + str(a)
    else :
      print "rozwiazania klasy (r, -(a/b) * r - (c/b)), gdzie r nalezy do liczb rzeczywistych, a a,b i c to odpowiednio " + str(a) + ", " + str(b) + ", " + str(c)
