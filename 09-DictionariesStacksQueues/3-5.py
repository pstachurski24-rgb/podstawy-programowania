def to_binary(number):
    if number < 0: raise ValueError('Only nonnegative integers')
    if number == 0: return '0'
    stack = []
    while number > 0:
        stack.append(str(number % 2))
        number //= 2
    digits = []
    while stack:
        digits.append(stack.pop())
    return ''.join(digits)
number = int(input('Natural number: '))
print('Binary number:', to_binary(number))
