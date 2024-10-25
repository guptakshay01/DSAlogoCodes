#   This file is created by Akshay Gupta
#   Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# My Solution --> O(n+m)
def merge_dicts(dict1, dict2):
    resDict = dict1.copy()
    if len(dict1) == 0:
        return dict2
    elif len(dict2) == 0:
        return dict1
    
    for key, value in dict2.items():
        resDict[key] = resDict.get(key, 0) + value

    return resDict

print(merge_dicts(dict1, dict2))