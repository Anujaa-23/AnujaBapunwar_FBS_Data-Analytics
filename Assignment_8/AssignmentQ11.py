def armstrong(n):
    sum = 0
    temp = n
    digits = len(str(n))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    return sum == n

n = int(input("Enter number: "))

if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")