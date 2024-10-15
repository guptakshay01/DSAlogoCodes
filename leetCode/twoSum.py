#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Find all pair of integers whose sum is equal to given number.

# Example
# List - [3,2,5,4,6,9]
# Num - 9
# Result - [5,4]


# Beginner Solution --> O(n^2)
def findPairs(ls, target):
    """
    Finds and prints all unique pairs of numbers in the given list that sum up to the specified number.
    """
    for i, vali in enumerate(ls):
        for _, valj in enumerate(ls[i+1:]):
            if vali == valj:
                continue
            if vali + valj == target:
                print(vali, valj)

findPairs([1,3,3,5,4,6,9,2], 6)


# Advance Solution --> O(n)
def findPairs_adv(ls, target):
    seen = {}

    for i, val in enumerate(ls):
        complement = target - val

        if complement in seen:
            return [seen[complement], i]
        
        seen[val] = i

indices = findPairs_adv([1,3,4,6,9,2], 6)
print(indices)