def word_replacement_2(string,word_list_to_replace,replacement):
    reduce_func = lambda string,word:string.replace(word,repl_wrd)
    from functools import reduce
    return reduce(reduce_func,word_list,test_str)
