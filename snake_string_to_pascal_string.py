def pascal_scale(string):
    l = string.split('_')
    string = [i.title() for i in l]
    return "".join(string)
