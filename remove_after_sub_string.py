def remove_after_substring(string,sub_string):
    l = string.split()
    i = 0
    l1 = []
    while l[i] != sub_string:
        l1.append(l[i])
        i += 1
        if l[i] == sub:
            l1.append(sub)
    return " ".join(l1)
