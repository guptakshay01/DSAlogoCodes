#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Given a list, write a function to get first, second best scores from the list.
#   List may contain duplicates.

myList = [84,85,86,90,85,90,85,83,23,45,84,1,2,0]

#   Solution --> O(n)
def firstSecond(myLs):
    first = 0
    second = 0

    for num in myList:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return first, second


print(firstSecond(myList))  # 90 86