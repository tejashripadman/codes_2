def minimum(l):
    minimum = l[0]
    for i in l[1:]:
        if i < minimum:
            minimum = i
    return minimum
