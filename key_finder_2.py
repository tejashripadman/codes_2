def key_finder(dictionary,key):
    '''This function takes list of dictionary and key as argument
    It returns a list of dictionary which contains given key'''
    return [i for i in dictionary if key in i.keys()]
