PDict = {(0,0):0.5}   # globalny słownik

def P(i, j):
    global PDict
    if (i,j) not in PDict:
      if i > 0 and j == 0:
        PDict[(i,j)] = 0.0
      elif j > 0 and i == 0:
        PDict[(i,j)] = 1.0
      else:
        PDict[(i,j)] = P(i-1,j) + P(i, j-1)
    return PDict[(i,j)]
