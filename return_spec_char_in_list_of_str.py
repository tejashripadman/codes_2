def return_specific_character(test_list,replacement_character,return_character):
    return [i if i == return_character else i.replace(i,replacement_character) for i in test_list ]
