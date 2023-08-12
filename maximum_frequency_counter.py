def maximum(s):
    """This function takes string as input and returns list with the characters having max frequency in string"""
    l = [s.count(i) for i in s]
    j = [i for i in set(s) if s.count(i)==max(l)]
    return(j)
