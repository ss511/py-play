"""
Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.

Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9
 2  5  8
 1  4  7
The given matrix is rotated by 90 degree
in anti-clockwise direction.

Input:
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
Output:
 4  8 12 16
 3  7 11 15
 2  6 10 14
 1  5  9 13
The given matrix is rotated by 90 degree
in anti-clockwise direction.

"""


def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(0, n):
        matrix[i].reverse()

    for i in range(0, n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[i][j], end="   ")
        print()


if __name__ == "__main__":
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print("Original Matrix: \n------- ")
    print_matrix(mat1)
    print("----------------------")
    print_matrix(mat2)
    print("----------------------")

    rotate_matrix(mat1)
    rotate_matrix(mat2)

    print("Rotated Matrix: \n-------")
    print_matrix(mat1)
    print("----------------------")
    print_matrix(mat2)

