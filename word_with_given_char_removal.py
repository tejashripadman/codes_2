def word_removal(test_list,char_list):
    for i in test_list[:]:
        for j in char_list:
            if j in i:
                test_list.remove(i)
    return test_list
