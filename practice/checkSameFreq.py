#   This file is created by Akshay Gupta
#   Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

def check_same_frequency(list1, list2):
    if len(list1) != len(list2):
        return False

    dictlist1 = {}
    dictlist2 = {}
    for item1, item2 in zip(list1, list2):
        dictlist1[item1] = dictlist1.get(item1, 0) + 1
        dictlist2[item2] = dictlist2.get(item2, 0) + 1
    
    return dictlist1 == dictlist2

print(check_same_frequency(list1, list2))