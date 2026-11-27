expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"
expression2 = "[(2+3]/4)"
expression3 = "(2-3*4+(5/6)"
def brackets_ok(expression):
    opening = []
    matching = {')':'(',']':'[','}':'{'}
    for char in expression:
        if char in '([{':
            opening.append(char)
        elif char in ')]}':
            if not opening or opening.pop() != matching[char]:
                return False
    return not opening
for expression in (expression1, expression2, expression3):
    print(expression, brackets_ok(expression))
