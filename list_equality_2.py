def list_equality(l1,l2):
  if len(l1) == len(l2):
    a = []
    for i in l1:
        if i in l2:
            a.append(True)
        else:
            a.append(False)
    if False in a:
        print(False)
    else:
        print(True)
  else:
      print(False)
