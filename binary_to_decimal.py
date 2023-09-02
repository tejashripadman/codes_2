def binary_to_decimal(lis):
    l1 = ["0b"+ele for ele in lis]
    return [int(ele,base=2) for ele in l1]
