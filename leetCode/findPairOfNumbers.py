#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.


# My solution --> O(n^2)
# space complexity --> O(n^2)
def pairSum(myList, sum):
    newList = []

    for idxi, val in enumerate(myList):
        for idxj in range(idxi+1, len(myList)):
            if val+myList[idxj] == sum:
                newList.append(str(val)+"+"+str(myList[idxj]))

    return newList


print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

# Referred solution --> O(n)
# space complexity --> O(n)
def pairSum2(myList, target_sum):
    seen = set()
    newList = []

    for val in myList:
        complement = target_sum - val
        if complement in seen:
            # Found a pair that sums up to target_sum
            newList.append(str(complement) + "+" + str(val))
        seen.add(val)  # Add the current number to the set

    return newList

print(pairSum2([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))