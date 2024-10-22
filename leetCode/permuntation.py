#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Given two lists of integers, determine whether they are permutations of each other.

#   Solution --> O(n logn)
def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    return list1.sort() == list2.sort()

print(permutation([1,2,3,4], [4,2,3,1]))