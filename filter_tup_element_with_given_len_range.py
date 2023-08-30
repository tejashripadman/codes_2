def filter_range_len_tuple(test_list,i,j):
    l = []
    for ele in test_list:
        if len(ele) >= i and len(ele) <=j:
            l.append(ele)
    return l
