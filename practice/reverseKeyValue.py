#   This file is created by Akshay Gupta
#   Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

my_dict = {'a': 1, 'b': 2, 'c': 3}


def reverse_dict(my_dict:dict):
    return {v:k for k, v in my_dict.items()}

print(reverse_dict(my_dict))