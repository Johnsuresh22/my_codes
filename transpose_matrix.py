def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print(transposed)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
