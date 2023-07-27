def print_multiple(l):
    l1 = set([i for i in l if l.count(i) > 1])
    for i in l1:
        print(i,end=' ')
