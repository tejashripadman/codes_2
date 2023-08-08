def unique_int_in_num(l):
  """ this function takes list of integers which returns list of numbers containing unique(non repeating)integers in it"""
  l1 = []
  for i in l:
    if len(set(str(i))) == len(str(i)):
      l1.append(i)
  return l1
