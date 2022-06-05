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


def matrix_transpose(matrix: list[list]):
    return square_matrix_transpose(matrix) if len(matrix) == len(matrix[0]) else non_square_matrix_transpose(matrix)


def matrix_trace(matrix: list[list]):
    # TODO: insert exeption if its not a square matrix
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace


def matrix_product(matrixA, matrixB):
    rows = len(matrixA)
    columns = len(matrixB[0])
    new_matrix = []
    for i in range(rows):
        new_matrix.append([None] * columns)

    i = 0
    j = 0
    for k in range(len(matrixA)):
        l = 0
        while l < len(matrixB[0]):
            m = 0
            value = 0
            while m < len(matrixB):
                value += matrixA[k][m] * matrixB[m][l]
                m += 1
            l +=1
            new_matrix[i][j] = value
            j += 1
        i += 1
        j = 0
    return new_matrix



