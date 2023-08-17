def string_replacement_detector(string,sub_string):
    '''This function takes an input string and a substring.
    It detects whether the sub string can be subtracted from input string multiple times till len of input string becomes zero or not'''
    for i in range(len(string)):
        if len(string)>0:
            string = string.replace(sub_string,"")
    if len(string)>0:
        return(False)
    else:
        return(True)
