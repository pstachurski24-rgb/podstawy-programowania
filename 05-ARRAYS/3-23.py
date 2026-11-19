
def is_subset(array1, array2):
    for element in array1:
        if element not in array2:
            return False
    return True


arr1 = [2, 4, 6]
arr2 = [1, 2, 3, 4, 5, 6, 7]

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Is subset:", is_subset(arr1, arr2))
