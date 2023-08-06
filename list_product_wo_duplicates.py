def list_prod(l):
  from functools import reduce
  return reduce(lambda x,y:x*y,set(l))
