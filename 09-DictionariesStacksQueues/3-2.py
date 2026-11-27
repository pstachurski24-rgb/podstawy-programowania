stack = []
for number in [2,3,7,4,1,9,8]:
    stack.append(number)
last_two_sum = stack.pop() + stack.pop()
print('Sum of last two:', last_two_sum)
remaining_sum = 0
while stack:
    remaining_sum += stack.pop()
print('Sum of remaining:', remaining_sum)
