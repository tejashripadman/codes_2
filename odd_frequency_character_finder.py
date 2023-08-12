def odd_freq(s):
    """This function takes string as input and returns list with the characters having odd frequency in string"""
    j = [i for i in set(s) if s.count(i)%2 != 0]
    return(j)
