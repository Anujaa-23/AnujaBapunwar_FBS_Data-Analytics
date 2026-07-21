# Program to calculate Simple Interest

p = float(input("Enter the Principal amount: "))
t = float(input("Enter the Time (in years): "))
r = float(input("Enter the Rate of Interest: "))

si = (p * t * r) / 100

print("Simple Interest =", si)