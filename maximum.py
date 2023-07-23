def maximum(l):
    maximum = l[0]
    for i in l[1:]:
        if i > maximum:
            maximum = i
    return maximum
