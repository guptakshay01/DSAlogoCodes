#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Write a function to remove the duplicate numbers on given integer array/list.

# My solution --> O(n^2)
def removeDuplicates(myLs):
    newLs = []
    for num in myLs:            # O(n)
        if num not in newLs:    # O(n)
            newLs.append(num)
    return newLs

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))


# Referred solution --> O(n)
def removeDuplicates2(myLs):
    newLs = []
    seen = set()
    for num in myLs:            # O(n)
        if num not in seen:     # O(1) --> sets are implemented as hash tables. Therefore, each membership check takes constant time.
            newLs.append(num)
            seen.add(num)
    return newLs

print(removeDuplicates2([1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 8]))