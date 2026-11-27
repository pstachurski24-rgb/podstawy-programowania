def calculate_rpn(tokens):
    stack = []
    for token in tokens:
        if token == '=': break
        if token in ('+','-','*','/'):
            if len(stack)<2: raise ValueError('Not enough operands')
            right = stack.pop()
            left = stack.pop()
            if token=='+': result=left+right
            elif token=='-': result=left-right
            elif token=='*': result=left*right
            else:
                if right==0: raise ZeroDivisionError('Division by zero')
                result=left/right
            stack.append(result)
        else:
            stack.append(float(token))
    if len(stack)!=1: raise ValueError('Invalid expression')
    return stack[0]
print('Type RPN tokens separated by spaces, ending with = (e.g. 2 3 + =)')
while True:
    value = input('RPN expression (blank = quit): ').strip()
    if not value: break
    try: print('Result:',calculate_rpn(value.replace('–','-').split()))
    except (ValueError, ZeroDivisionError) as error: print('Error:',error)
