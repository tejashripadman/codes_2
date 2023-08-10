def vowels_detector(s):
  """This functions takes string as input and returns true if any of the vowel is absent in string else false"""
    a = "aeiou"
    l = []
    for i in s:
        if i in a:
            l.append(i)
    if len(set(l)) == len(s):
        return "accepted"
    else:
        return "Not accepted"
