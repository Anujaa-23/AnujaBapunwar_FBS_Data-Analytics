# Program to find the roots of a quadratic equation

import math

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

d = b**2 - 4*a*c

root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

print("First Root =", root1)
print("Second Root =", root2)