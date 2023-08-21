def return_specific_character(test_list,replacement_character,return_character):
    l = []
    for i in test_list:
        if i != return_character:
            l.append(replacement_character)
        else:
            l.append(i)
    return l
