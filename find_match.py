def find_match(str1,str2):
  """This function takes two strings as argument and returns the count of charachers which are found in both the strings"""
    l = [i for i in str1 if i in str2]
    return(len(set(l)))
