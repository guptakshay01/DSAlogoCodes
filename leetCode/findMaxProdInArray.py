#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Find the maximum product of two integers in an array where all elements are positive.

arr = [1, 7, 3, 4, 9, 5] 

# Solution --> O(n)
def max_product(arr):
    max1 = 0
    max2 = 0

    for val in arr:
        if val > max1:
            max2 = max1
            max1 = val
        elif val > max2:
            max2 = val

    return max1 * max2

print(max_product(arr))