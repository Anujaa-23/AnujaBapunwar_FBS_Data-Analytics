# Function for 1 + 2 + ... + n
def sum1(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


# Function for 1! + 2! + ... + n!
def sum2(n):
    s = 0
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact = fact * j
        s = s + fact
    return s


# Function for 1^1 + 2^2 + ... + n^n
def sum3(n):
    s = 0
    for i in range(1, n + 1):
        s = s + (i ** i)
    return s

n = int(input("Enter n: "))

print("Sum of 1+2+...+n =", sum1(n))
print("Sum of 1!+2!+...+n! =", sum2(n))
print("Sum of 1^1+2^2+...+n^n =", sum3(n))