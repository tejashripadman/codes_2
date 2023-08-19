def word_replacement_4(test_str,map_dict):
    return "".join([idx if idx not in map_dict.keys() else map_dict[idx] for idx in test_str])
