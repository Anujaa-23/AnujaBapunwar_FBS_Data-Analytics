# Program to calculate Compound Interest

P = float(input("Enter Principal (P): "))
T = float(input("Enter Time (T) in years: "))
R = float(input("Enter Rate (R): "))

A = P * (1 + R / 100) ** T

CI = A - P

print("Compound Interest =", round(CI, 2))
print("Amount =", round(A, 2))