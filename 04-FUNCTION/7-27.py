
def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    digit_sum = sum(int(digit) for digit in product_code[:3])
    control_digit = digit_sum % 7

    return control_digit == int(product_code[3])


print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
