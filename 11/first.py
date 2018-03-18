
import random
import numpy

def randA(N) :
  rnd = []
  for i in range(0,N):
    rnd.append(random.randint(0, N - 1))
  return rnd

def randB(N) :
  rnd = []
  for i in range(0,N):
    rnd.append(random.randint(0, N - 1))
  rnd.sort()
  for x in range(N/20):
    i = random.randint(0, len(rnd) - 1)
    j = random.randint(0, len(rnd) - 1)
    rnd[i], rnd[j] = rnd[j], rnd[i]
  return rnd
  
def randC(N) :
  r = randB(N)
  r.reverse()
  return r
  
def randD(N) :
  r = numpy.random.normal(size=N)
  return r
  
def randE(N, k) :
  if k > N :
    raise ValueError("k>N")
  rnd = []
  for i in range(0,N):
    rnd.append(random.randint(0, k - 1))
  return rnd




