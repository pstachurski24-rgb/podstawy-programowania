
arr = [-15, 8, -31, 47, -2, 19]

minimum = arr[0]
maximum = arr[0]

for number in arr:
    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

print("Minimum:", minimum)
print("Maximum:", maximum)
