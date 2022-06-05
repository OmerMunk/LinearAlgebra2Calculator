from utils.swaps import matrix_elements_swap

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]}\t", end="")
        print("\n")

def square_matrix_transpose(matrix: list[list]):
    i = 0
    j = 1
    while i < len(matrix):
        while j < len(matrix[0]):
            matrix_elements_swap(matrix, i, j, j, i)
            j += 1
        i += 1
        j = i + 1
    return matrix


def non_square_matrix_transpose(matrix: list[list]):
    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = []
    for i in range(columns):
        new_matrix.append([None] * rows)
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[0]):
            new_matrix[j][i] = matrix[i][j]
            j += 1
        i += 1

    return new_matrix