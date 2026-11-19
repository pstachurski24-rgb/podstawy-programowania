
def convert_to_1d(arr):
    result = []

    for row in arr:
        for value in row:
            result.append(value)

    return result


arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

for arr in arrays:
    print("2D array:", arr)
    print("1D array:", convert_to_1d(arr))
    print()
