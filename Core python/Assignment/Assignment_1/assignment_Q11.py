# Program to find the area and circumference of a circle

import math

radius = int(input("Enter the radius of the circle: "))

area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("Area of the circle =", area)
print("Circumference of the circle =", circumference)