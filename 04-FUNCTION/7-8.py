
def f(amount_to_pay):
    if amount_to_pay < 0:
        return 0

    coins = 0

    coins += amount_to_pay // 5
    amount_to_pay %= 5

    coins += amount_to_pay // 2
    amount_to_pay %= 2

    coins += amount_to_pay

    return coins


print(f(23))
print(f(8))
print(f(2))
print(f(0))
