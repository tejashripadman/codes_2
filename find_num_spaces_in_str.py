def spaces(string):
  a = sum(not i.isspace() for i in string)
  return a
