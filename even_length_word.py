def print_even_len_word(string):
    s = string.split()
    for i in s:
        if len(i) % 2 ==0:
            print(i)
