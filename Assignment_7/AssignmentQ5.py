n = 5

for i in range(1, n + 1):

    for j in range(n - i):
        print("  ", end="")

    print("1", end=" ")

    if i == n:
        for j in range(2, n + 1):
            print(j, end=" ")
    elif i > 1:
        for j in range(2 * i - 3):
            print("  ", end="")
        print(i, end=" ")

    print()