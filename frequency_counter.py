def frequency_counter(string):
    '''This function takes a string and returns a dictionary which counts the frequency of words in given string'''
    test = string.split()
    return {i:test.count(i) for i in test}
