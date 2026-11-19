
def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)


print("5^3 =", power(5, 3))
