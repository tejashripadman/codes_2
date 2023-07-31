def empty_list_remover(l):
  for i in l:
    if i == []:
        l.remove(i)
  return l
