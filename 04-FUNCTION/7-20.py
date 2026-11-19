
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def f(n):
    count = 0
    number = 1

    while count < n:
        number += 1

        if is_prime(number):
            count += 1

    return number


print(f(1))
print(f(5))
