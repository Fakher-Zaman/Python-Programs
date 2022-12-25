A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B)):
        C[i][j] = A[i][j] + B[i][j]

for r in C:
    print(r)