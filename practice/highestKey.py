#   This file is created by Akshay Gupta
#   Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

dict1 = {'a': 5, 'b': 9, 'c': 2}

# My Solution --> O(n)
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

print(max_value_key(dict1))