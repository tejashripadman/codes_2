def word_frequency_counter(l):
  """This function takes a list of string and returns the frequency of each word in the string in form of dictionary"""
  l = " ".join(l) #Creates continuous str from list
  l = l.split() # creates the dictionary of the words
  d = {}
  s = set(l)
  for i in s:
    d[i] = l.count(i)/len(l)
  return d
