x = float(input("x = "))
y = float(input("y = "))

if x == 0 and y == 0:
    print("Point is at (0,0)")
elif x == 0:
    print("Point is on Y axis")
elif y == 0:
    print("Point is on X axis")
elif x > 0 and y > 0:
    print("Point is in the first quadrant")
elif x < 0 and y > 0:
    print("Point is in the second quadrant")
elif x < 0 and y < 0:
    print("Point is in the third quadrant")
else:
    print("Point is in the fourth quadrant")