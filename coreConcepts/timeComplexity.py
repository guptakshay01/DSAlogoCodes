#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   HERE I DEMONSTRATE ALL THE BIG-O TIME COMPLEXITIES

####  O(1) - Constant Time Complexity  ####
print("O(1) - Constant Time Complexity")
print("Hello World")



####  O(n) - Linear Time Complexity  ####
print("O(n) - Linear Time Complexity")
for i in range(1, 10):
    print(i*i)



####  O(n^2) - Quadratic Time Complexity  ####
print("O(n^2) - Quadratic Time Complexity")
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j)



####  O(log n) - Logrithmic Time Complexity  ####
print("O(log n) - Logrithmic Time Complexity")
n = 1
sum = 1
while n < 100:
    sum += n
    n *= sum
print(sum)

for i in range(1, 100, 3):
    print(i)



####  O(2^n) - Exponential Time Complexity  ####
print("O(2^n) - Exponential Time Complexity")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)



####  O(m+n) - Addition Time Complexity  ####
print("O(m+n) - Addition Time Complexity")
for i in range(1, 10):
    print(i*i)

for i in range(1, 20):
    print(i*i)



####  O(m*n) - Multiplication Time Complexity  ####
print("O(m*n) - Multiplication Time Complexity")
for i in range(1, 10):
    print(i*i)
    for j in range(1, i):
        print(j*j)



sampleArray = [11,32,34,49,57,16,7,28,93,140,110,2]
####  Iterative algorithm - finding the largest number in the array  ####
print("Given array: ", sampleArray)
def getLargestNum(arr):
    largestNum = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > largestNum:
            largestNum = arr[i]
    return largestNum
print("Iterative algorithm - Largest number is",getLargestNum(sampleArray), "and time complexity is: O(n)")


####  Recursive algorithm - finding the largest number in the array  ####
def getMaxNumRec(arr, n):
    if n == 1:
        return sampleArray[0]
    return max(sampleArray[n-1], getMaxNumRec(sampleArray, n-1))

print("Recursive algorithm - Largest number is",getLargestNum(sampleArray), "and time complexity is: O(2^n)")


