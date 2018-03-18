import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if not 2 * max(a, b, c) < (a + b + c):
      raise ValueError("not a triangle")
    s = a + b + c / 2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

