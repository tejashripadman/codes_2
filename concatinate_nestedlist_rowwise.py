def concatinate_nested_list_row_wise(list1,list2):
  for i,j in zip(list1,list2):
    i.extend(j)
  return list1
