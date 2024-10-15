#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Find Missing Number in array having numbers 1 to 100

def missing_number(arr, n):

    # Calculate sum of n natural numbers
    total = n * (n+1) // 2

    # Calculate sum of numbers in the array
    sum_arr = sum(arr)

    # Missing number
    return total - sum_arr

print(missing_number([1, 2, 4, 5, 6], 6))