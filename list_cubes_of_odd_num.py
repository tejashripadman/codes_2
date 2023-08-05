def cube_odd_num(l):
  """It returns a list of cube of odd numbers in input list"""
  l1 = [i**3 for i in l if i%2]
  return l1
