def vowels_remover(string):
    vowels = 'aeiou'
    l = []
    s = ''
    for i in string:
        if i not in vowels:
            s += i
        elif len(s)>0 and i in vowels:
            l.append(s)
            s = ''
    return l
