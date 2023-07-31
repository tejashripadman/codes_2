def maximum_product_finder(l):
  l1 = []
  for i in l:
    prod = 1
    for j in i:
        prod *= j
    l1.append(prod)
  return max(l1)
