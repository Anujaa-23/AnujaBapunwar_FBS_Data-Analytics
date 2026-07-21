# Find the sum of three-digit number.

num = int(input("Enter a three-digit number: "))

d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

sum_digits = d1 + d2 + d3

print("Sum of digits =", sum_digits)