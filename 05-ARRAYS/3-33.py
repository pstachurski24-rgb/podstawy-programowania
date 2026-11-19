
arr = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

minimum = maximum = arr[0][0]
min_row = min_col = 0
max_row = max_col = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < minimum:
            minimum = arr[i][j]
            min_row, min_col = i, j

        if arr[i][j] > maximum:
            maximum = arr[i][j]
            max_row, max_col = i, j

print("Minimum:", minimum)
print("Row:", min_row + 1, "Column:", min_col + 1)

print("Maximum:", maximum)
print("Row:", max_row + 1, "Column:", max_col + 1)
