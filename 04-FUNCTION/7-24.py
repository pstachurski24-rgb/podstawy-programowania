
def f(expression):
    result = 0
    sign = 1

    for char in expression:
        if char == "+":
            sign = 1
        elif char == "-":
            sign = -1
        else:
            result += sign * int(char)

    return result


print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
