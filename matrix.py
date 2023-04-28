import numpy as np


def my_matmul(A, B):

    if not isinstance(B, np.ndarray):
        B = np.array(B)

    if len(A[0]) != B.shape[0]:
        print("Matrices are not compatible for multiplication.")
        return None

    if len(B.shape) == 1:
        C = [0 for i in range(len(A))]
    else:
        C = [[0 for j in range(B.shape[1])] for i in range(len(A))]


    if len(B.shape) == 1:
        for i in range(len(A)):
            dot_product = 0
            for j in range(B.shape[0]):
                dot_product += A[i][j] * B[j]
            C[i] = dot_product
    else:
        for i in range(len(A)):
            for j in range(B.shape[1]):
                dot_product = 0
                for k in range(len(A[0])):
                    dot_product += A[i][k] * B[k][j]
                C[i][j] = dot_product

    return C


def my_add(arr1, arr2):

    arr1 = np.asarray(arr1)
    arr2 = np.asarray(arr2)

    if arr1.shape != arr2.shape:
        raise ValueError("The two input arrays must have the same shape.")

    result = np.zeros_like(arr1)
    for i in range(arr1.shape[0]):
        result[i] = arr1[i] + arr2[i]

    return result


def my_jacobiMethod_itteration(N, B, M, x1, numberOfIterration):

    for i in range(numberOfIterration):
        x2 = my_matmul(N, B)
        x2 = my_add(x2, my_matmul(M, x1))
        x1 = x2

    return f"Znalezione rozwiazania ukladu przy zadanej liczbie iteracji: {numberOfIterration} \n {x1}"


def my_jacobiMethod_epsilon(N, B, M, x1, eps):
    x2 = np.matmul(N, B)
    x2 = np.add(x2, np.matmul(M, x1))

    while max(np.abs(np.subtract(x1, x2))) > eps:
        x1 = x2
        x2 = my_matmul(N, B)
        x2 = my_add(x2, my_matmul(M, x1))

    return f"Znalezione rozwiazania ukladu przy zadanej dokladnosci: {eps} \n {x1}"


