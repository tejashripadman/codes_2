def element_remover(l,a):
  for i in l[:]:
    if i > a:
        l.remove(i)
  return l
