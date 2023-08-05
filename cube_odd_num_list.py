def cube(n):
  return lambda n: n**3
def odd(n):
  return n if n%2
def cube_odd_num(l):
  return list(filter(odd,map(cube,l)))
  
