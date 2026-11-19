
def bubblesort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


arr1 = [9, 3, 7, 1, 5]
arr2 = [20, 4, 15, 8, 2]
arr3 = [100, 50, 75, 25, 10]

print("Sorted array 1:", bubblesort(arr1))
print("Sorted array 2:", bubblesort(arr2))
print("Sorted array 3:", bubblesort(arr3))
