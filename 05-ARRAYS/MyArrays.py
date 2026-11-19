
def second_largest(arr):
    ordered = arr[:]
    for i in range(len(ordered)):
        for j in range(len(ordered) - 1 - i):
            if ordered[j] > ordered[j + 1]:
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]

    for i in range(len(ordered) - 2, -1, -1):
        if ordered[i] != ordered[-1]:
            return ordered[i]
    return None


def difference(arr):
    smallest = largest = arr[0]
    for n in arr:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return largest - smallest


def median(arr):
    ordered = arr[:]
    for i in range(len(ordered)):
        for j in range(len(ordered) - 1 - i):
            if ordered[j] > ordered[j + 1]:
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]

    n = len(ordered)
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2


def min_max(arr):
    smallest = largest = arr[0]
    for n in arr:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return [smallest, largest]


def to_string(arr):
    result = ""
    for i in range(len(arr)):
        if i > 0:
            result += "-"
        result += str(arr[i])
    return result
