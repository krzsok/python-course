def flatten(S):
  result = []
  for s in S:
    if isinstance(s,(list, tuple)):
      result.append(flatten(s))
    else:
      result.append(s)
  return result
