def word_with_specific_length(string,k):
    """This function takes string and length of words and returns a list with word having the length greater than or
    equal to given value"""
    l = string.split()
    j = [i for i in l if len(i)>=k]
    return j
