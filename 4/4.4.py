def fib(n):
  f1 = 0
  f2 = 1
  
  if n == 0:
    return 0
    
  elif n == 1:
    return 1
  
  else:
    for x in range(2,n):
      temp = f2
      f2 = f1 + f2
      f1 = temp
  
  return f1+f2    
    
