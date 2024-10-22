#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Given 2D list calculate the sum of diagonal elements.

myList2D = [[1,2,3],[4,5,6],[7,8,9]]

# Solution --> O(?)
def diagonalSum(matrix):

    matrixLen = len(matrix)
    diagonal1 = 0
    diagonal2 = 0

    for i in range(matrixLen):
        diagonal1 += matrix[i][i]
        diagonal2 += matrix[i][matrixLen - i - 1]

    if matrixLen % 2 == 1:
        middle = matrix[matrixLen//2][matrixLen//2]
        return diagonal1 + diagonal2 - middle

    return diagonal1 + diagonal2


print(diagonalSum(myList2D))