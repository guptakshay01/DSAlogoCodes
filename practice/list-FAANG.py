#   This file is created by Akshay Gupta
#   10 FAANG-level Python programming problems that focus on lists

# Two Sum
#     Problem: Given a list of integers and a target value, return the indices of two numbers such that they add up to the target.
#     Constraints: You may assume that each input would have exactly one solution, and you cannot use the same element twice.
#     Example Input: nums = [2, 7, 11, 15], target = 9
#     Example Output: [0, 1]

nums = [3, 7, 8, 2, 6, 11, 15]
target = 9

def twoSum(ls, tgt):
    diff = 0
    numToIndex = {}
    for idx, num in enumerate(ls):
        diff = tgt - num
        if diff in numToIndex:
            return numToIndex[diff], idx
        numToIndex[num] = idx
    return None

# print(twoSum(nums, target))


# Container with Most Water
#     Problem: Given a list of non-negative integers representing heights where each element is a vertical line on the x-axis,
#              find two lines that, together with the x-axis, form a container that holds the most water.
#     Constraints: Try to solve the problem in O(n) time.
#     Example Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#     Example Output: 49
#     Approach: Use the two-pointer technique to find the maximum area.

def largestContainer(htList):
    maxArea = 0
    left = 0
    right = len(htList) - 1
    lgt = len(htList)

    while right > left:
        if htList[left] < htList[right]:
            left += 1
            lgt -= 1
        elif htList[left] == htList[right]:
            prod = htList[left] * lgt
            left += 1
            right -= 1
            lgt -= 2
        else:
            right -= 1
            lgt -= 1
        
        if maxArea < prod:
            maxArea = prod
    
    return maxArea

print(largestContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))