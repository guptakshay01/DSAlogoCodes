#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   How to check if an array contains a number

import numpy as np

npArr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# Linear Search --> O(n)
def findElement(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return "number found"
    
    return "number not found"


print(findElement(npArr, 3))