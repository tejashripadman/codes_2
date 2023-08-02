def repetition_detector(string):
    l = [i for i in string]
    if len(l) ==  len(set(l)):
        return False
    else:
        return True
