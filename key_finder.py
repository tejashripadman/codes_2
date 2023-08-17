def key_finder(dictionary,key):
    '''This function takes list of dictionary and key as argument
    It returns a list of dictionary which contains given key'''
    l = []
    for i in test_list:
        if key in i.keys():
            l.append(i)
    return l
