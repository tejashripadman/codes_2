def count_even_odd(l):
  l1 = sum(1 for i in l if i % 2 == 0)
  l2 = sum(1 for i in l if i % 2 != 0)
  return f"even numbers are {l1} and odd numbers are {l2}"
