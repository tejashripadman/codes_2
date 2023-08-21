def list_filter_using_index_in_second_list(test_list1,test_list2,sub_str):
    l = []
    for i,j in enumerate(test_list2):
        if sub_str in j:
            l.append(test_list1[i])
    return l
