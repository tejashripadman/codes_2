def positive_negative_num_counter(a,b,c):
    l1 = sum(1 for i in range(a,b,c) if i > 0)
    l2 = sum(1 for i in range(a,b,c) if i < 0)
    return l1,l2
