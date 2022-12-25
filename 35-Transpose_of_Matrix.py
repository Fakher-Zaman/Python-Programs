# Solution # 1 (By Using Nested for Loop):
# matrix = [[1, 2, 3],
#           [4, 5, 6]]

# transpose = [[0, 0],
#              [0, 0],
#              [0, 0]]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transpose[j][i] = matrix[i][j]

# for r in transpose:
#     print(r)

# Solution # 2 (By using list comprehension):
matrix = [[1, 2, 3],
          [4, 5, 6]]

transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for r in transpose:
    print(r)