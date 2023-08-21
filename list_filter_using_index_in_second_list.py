def list_filter_using_index_in_second_list(test_list1,test_list2,sub_str):
    return [i for i,j in zip(test_list1,test_list2) if sub_str in j]
