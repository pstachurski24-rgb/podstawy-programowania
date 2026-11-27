# 1-5: Area and perimeter of two squares
class Square:
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return 4 * self.a

for side in (4, 6):
    square = Square(side)
    print(f"Square with side {side}:")
    print(f"Area is {square.area()}, Perimeter is {square.perimeter()}")
