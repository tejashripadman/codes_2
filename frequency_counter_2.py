def frequency_counter(string):
    '''This function takes a string and returns a dictionary which counts the frequency of words in given string'''
    test = string.split()
    d = {}
    for i in test:
        d[i] = test.count(i)
    return d
