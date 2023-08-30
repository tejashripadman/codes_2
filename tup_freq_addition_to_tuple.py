def tup_freq_addition_to_tup(test_list):
    d = {i:test_list.count(i) for i in test_list}
    l1 = []
    for i,j in d.items():
        l = []
        l.extend(list(i))
        l.extend([j])
        l1.append(tuple(l))
    return l1
