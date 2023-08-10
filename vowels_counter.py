def vowels_counter(s):
  """this function taskes string as input and returns count of vowels present in given string"""
    a = "aeiou"
    l = [i for i in s if i in a]
    return len(l)
