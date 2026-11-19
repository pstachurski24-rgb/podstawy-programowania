
arr = [2, 3, 7, 5, 4]

print("Array:", arr)
print("Number of elements:", len(arr))
print("First value:", arr[0])
print("Second value:", arr[1])
print("Last value:", arr[-1])
print("Last but one:", arr[len(arr) - 2])
print("Sum:", arr[0] + arr[-1])
print("Middle:", arr[len(arr) // 2])

for value in arr:
    print(value, end=" ")
