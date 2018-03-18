import random
import math

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    inCircleCount = 0
    inSquareCount = 0
    pi = 0
    
    for i in range(0,n):
        x = random.random()
        y = random.random()
        if(x**2+y**2 < 1):
                   inCircleCount+= 1
        inSquareCount+= 1
    pi = 4.0*inCircleCount/inSquareCount
    
    return pi

        
