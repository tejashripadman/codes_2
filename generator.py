def generator(start,end,step):
    i = start
    while i <= end:
        yield i
        i += step
