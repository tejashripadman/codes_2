def potential_word_seperator(string):
    s = ''
    for ele in string:
        if ele.isupper():
            s = s+" "+ele
        else:
            s += ele
    return(s)
