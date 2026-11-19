
def f(dice):
    if not dice:
        return None

    best_digit = dice[0]
    best_count = 1
    current_count = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > best_count:
            best_count = current_count
            best_digit = dice[i]

    return int(best_digit)


print(f("5233165554211"))
print(f("2133"))
