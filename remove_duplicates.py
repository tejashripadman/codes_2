def remove_duplicates(s):
  """This function takes as tring as an argument and returns a string contaiing unique characters present in input string"""
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    return"".join(l)
