Write a Python program to create an array and perform addition of two matrices. 

# Assignment 4: Addition of Two Matrices

# First Matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Second Matrix
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Result Matrix
result = []

# Matrix Addition
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Display Result
print("Addition of Two Matrices:")
for row in result:
    print(row)