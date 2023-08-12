def minimum(s):
    """This function takes string as input and returns list with the characters having least frequency in string"""
    l = [s.count(i) for i in s]
    j = [i for i in s if s.count(i)==min(l)]
    return(j)
