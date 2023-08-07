def remove_common(a,b):
  l = [i for i in a if i not in b]
  l2 = [i for i in b if i not in a]
  return l+l2
