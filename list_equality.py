def list_equality(l1,l2):
  if len(l1) == len(l2):
    return(all(i in l2 for i in l1))
  else:
    return(False)
