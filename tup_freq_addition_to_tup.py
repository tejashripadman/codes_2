def tup_freq_addition_to_tup(test_list):
    d = {}
    for i in test_list:
        d[i] = test_list.count(i)
    l1 = []
    for i in d.keys():
        l = []
        l.extend(i)
        l.extend([d[i]])
        l1.append(tuple(l))
    return l1
