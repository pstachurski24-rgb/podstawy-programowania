def reverse_text(text):
    stack = list(text)
    result = []
    while stack:
        result.append(stack.pop())
    return ''.join(result)
text = input('Text to reverse: ')
print(reverse_text(text))
