def sum_seq(S):
  sum=0
  for s in S:
    if isinstance(s,(list, tuple)):
      sum +=  sum_seq(s)
    else:
      sum += s
  return sum
