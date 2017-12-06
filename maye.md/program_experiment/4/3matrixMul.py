def matrixMul(A,B):
    n = input()
    r = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j] += A[i][k] * B[k][j]
    return r
a = input()
b = input()
print matrixMul(a,b)

