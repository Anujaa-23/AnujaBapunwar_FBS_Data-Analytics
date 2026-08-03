def prime_sum(n):
    sum = 0

    for num in range(2, n+1):
        count = 0

        for i in range(1, num+1):
            if num % i == 0:
                count += 1

        if count == 2:
            sum += num

    return sum

n = int(input("Enter n: "))
print("Sum of prime numbers =", prime_sum(n))