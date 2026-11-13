# Distance to horizon

import math

height = float(input("Enter height in meters: "))

distance = 3.57 * math.sqrt(height)

print("Distance to horizon:", round(distance, 2), "km")