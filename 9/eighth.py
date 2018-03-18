def bst_max(top):
  if top is None  :
    raise ValueError("tree is empty")
  if top.right is None :
    return top.data
  temp = top.right
  while temp.right is not None :
    temp = temp.right
  return temp.data  

def bst_min(top):
  if top is None :
    raise ValueError("tree is empty")
  if top.left is None :
    return top.data
  temp = top.left
  while temp.left is not None :
    temp = temp.left
  return temp.data
