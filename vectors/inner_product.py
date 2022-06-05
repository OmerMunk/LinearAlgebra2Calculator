from Exceptions.vector_exceptions import DifferentVectorsLength


def standart_inner_product(vector1: list, vector2: list):
    length = len(vector1)
    if len(vector2) != length:
        raise DifferentVectorsLength
    result = 0
    for i in range(length):
        result += vector1[i] * vector2[i]
    return result
