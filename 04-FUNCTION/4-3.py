
import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p-a) * (p-b) * (p-c))
    return area

print(triangle_area(3, 4, 5))
print(triangle_area(5, 12, 13))
print(triangle_area(7, 24, 25))

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a:
    print("Area:", triangle_area(a, b, c))
else:
    print("Invalid triangle")
