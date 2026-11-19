
from ranges import in_range

number = 7
x = 2
y = 15

result = in_range(number, x, y)

print("A number:", number)
print(f"Number {number} in range <{x},{y}>:",
      "yes" if result else "no")
