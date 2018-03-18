def odwracanie(L, left, right):
  while left != right:
    temp = L[left]
    L[left] = L[right]
    L[right] = temp
    left += 1
    right -= 1
    
  return L
