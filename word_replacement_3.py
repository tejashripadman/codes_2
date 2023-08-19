def word_replacement_3(string,map_dictionary):
    for key in map_dictionary.keys():
        if key in string:
            string = string.replace(key,map_dictionary[key])
    return string
