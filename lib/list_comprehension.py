#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [n for n in num_list if n % 2 == 0]
    return new_list
    pass

def make_exclamation(sentence_list):
    new_list = [string + '!' for string in sentence_list]
    return new_list
    pass