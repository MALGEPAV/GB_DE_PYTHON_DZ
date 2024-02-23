def my_transpose(matrix: list[list]):
    dim = len(matrix)
    for i in range(0, dim - 1):
        for j in range(i + 1, dim):
            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# m = [[1, 2], [3, 4]]
# m = [[1]]
print("Initial matrix:")
for row in m:
    print(*row)

my_transpose(m)

print("Transposed matrix:")
for row in m:
    print(*row)
