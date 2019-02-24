import numpy as np
def matmult(A = [], B = []):
    result = np.zeros((len(A[0]), len(B)))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A)):
                result[i][j] += A[i][k] * B[k][j]
    return (A, B, result)
if __name__ == "__main__":
    print(matmult([[1, 2], [2, 3]], [[3, 5],[4, 6]]))