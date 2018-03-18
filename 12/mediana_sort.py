def mediana_sort(L, left, right):
  slist = L[left : right + 1]
  slist.sort()
  lng = len(slist)
  if lng % 2 == 0 :
    return (slist[(lng / 2 - 1)] + slist[(lng / 2)]) / 2.0
  else :
    return slist[(lng / 2)]
  
