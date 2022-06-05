from matrix.matrix_operations import matrix_trace, matrix_product, non_square_matrix_transpose


def standard_matrix_inner_product(matrixA, matrixB):
    return matrix_trace(matrix_product(non_square_matrix_transpose(matrixB), matrixA))


