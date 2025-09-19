def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10, 11, 12]]

C = [[7, 8],
     [9, 10],
     [11, 12]]
print("\nAddition of A and B:")
for row in add_matrices(A, B):
    print(row)
    
print("\nMultiplication of A and C:")
for row in multiply_matrices(A, C):
    print(row)
