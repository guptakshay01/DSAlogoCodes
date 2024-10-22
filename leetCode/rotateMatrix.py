#   This file is created by Akshay Gupta

#   You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#   You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#   DO NOT allocate another 2D matrix and do the rotation.

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# My Solution --> O(n^2)
def rotate(matrix):
    matrixLen = len(matrix)

    # Transpose of matrix
    for idxI in range(matrixLen):
        for idxJ in range(idxI, matrixLen):
            if idxI != idxJ:
                matrix[idxJ][idxI], matrix[idxI][idxJ]= matrix[idxI][idxJ], matrix[idxJ][idxI]
    
    # Reversing the rows
    for idxI in range(matrixLen):
        for idxJ in range(matrixLen//2):
            matrix[idxI][idxJ], matrix[idxI][matrixLen-idxJ-1] = matrix[idxI][matrixLen-idxJ-1], matrix[idxI][idxJ]

    return matrix

print(rotate(matrix))

# Referred Solution --> O(n^2) --> More Pythonic
def rotate2(matrix):
    # Step 1: Transpose the matrix using zip
    matrix[:] = zip(*matrix)    #   zip() transposes the matrix by unpacking the matrix rows and then zipping them together.

    # Step 2: Reverse each row
    matrix[:] = [list(row)[::-1] for row in matrix]

    return matrix

print(rotate2(matrix))



# Example of zip function
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = [True, False, None]

# zipped = zip(list1, list2, list3)
# print(list(zipped))
# [(1, 'a', True), (2, 'b', False), (3, 'c', None)]

# Unzip example
# zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
# list1, list2 = zip(*zipped)

# print(list1)
# print(list2)
# (1, 2, 3)
# ('a', 'b', 'c')