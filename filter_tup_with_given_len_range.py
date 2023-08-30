def filter_range_len_tuple(test_list,i,j):
    return [ele for ele in test_list if len(ele)>=i and len(ele)<=j]
