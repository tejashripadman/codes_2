def word_replacement(string,word_list_to_replace,replacement):
    for i in word_list_to_replace:
        if i in word_list_to_replace:
            string = string.replace(i,replacement)
    return string
