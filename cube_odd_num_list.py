def cube(n):
    return n**3
def odd(n):
    if n % 2:
        return n
def cube_odd_num(l):
    return list(filter(odd,map(cube,l)))
  
