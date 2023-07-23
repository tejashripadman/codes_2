def multiplication(l):
    l = [int(i) for i in l]
    mul = l[0]
    for i in l[1:]:
        mul *= i
    return mul
