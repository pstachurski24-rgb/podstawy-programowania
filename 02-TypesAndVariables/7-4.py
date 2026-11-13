import math

circumference = float(input("Enter tree circumference in cm: "))

diameter = circumference / math.pi

# TODO
can_be_cut = diameter >= ...

print(f"Tree can be cut down: {can_be_cut}")