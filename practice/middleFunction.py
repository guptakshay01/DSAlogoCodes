#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

arr = [1, 7, 3, 4, 9, 5]

# Solution --> O(?)
def middleFunc(arr):
    return arr[1:-1]

print(middleFunc(arr))