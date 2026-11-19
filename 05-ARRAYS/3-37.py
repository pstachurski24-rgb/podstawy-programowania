
def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])

    result = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(m[i][j])
        result.append(row)

    return result


def print_matrix(matrix):
    for row in matrix:
        print(*row)


matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]]
]

for matrix in matrices:
    print("Original:")
    print_matrix(matrix)

    print("Transposed:")
    print_matrix(transpose_matrix(matrix))
    print()
