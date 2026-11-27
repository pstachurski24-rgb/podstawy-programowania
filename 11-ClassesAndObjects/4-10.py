# 4-10: Check whether at least n points belong to the first quadrant
class C:
    def __init__(self, points):
        self.points = points

    def m(self, n):
        return sum(1 for x, y in self.points if x > 0 and y > 0) >= n

points = C([[2, 3], [1, 8], [-6, 4], [3, -7]])
print(points.m(2))  # True
print(points.m(3))  # False
