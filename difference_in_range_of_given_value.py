def difference(l,k):
  """This function takes list as input and returns true if the difference between the max element and min element in the list lies within given range"""
  if (max(l)-min(l)) in range(k):
    return True
  else:
    return False
