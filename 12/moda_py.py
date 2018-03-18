def moda_py(L, left, right): 
  slist = L[left : right + 1]
  occurences = {el:0 for el in slist}
  for el in slist :
    occurences[el] += 1

  v=list(occurences.values())
  k=list(occurences.keys())
  return k[v.index(max(v))]
