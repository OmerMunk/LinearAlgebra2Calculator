def vector_elemets_swap(vector, i, j):
    temp = vector[i]
    vector[i] = vector[j]
    vector[j] = temp


def matrix_elements_swap(matrix, i, j, k, l):
    temp = matrix[i][j]
    matrix[i][j] = matrix[k][l]
    matrix[k][l] = temp
