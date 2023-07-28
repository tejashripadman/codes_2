def lower_upper_case_string(test_string):
  ind = len(test_string)//2
  return test_string[:ind].lower()+test_string[ind:].upper()
