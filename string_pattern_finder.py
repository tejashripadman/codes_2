def string_pattern_match(test_str,k):
    for i in test_str:
        if i not in k:
            test_str = test_str.replace(i,'')
    if k in test_str:
        return True
    else:
        return False
