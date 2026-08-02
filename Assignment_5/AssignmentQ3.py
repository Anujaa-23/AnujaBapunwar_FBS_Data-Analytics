n = int(input("Enter number of passengers: "))
ticket = int(input("Enter ticket cost: "))

total = 0

for i in range(n):
    age = int(input("Enter age: "))

    if age < 12:
        amount = ticket * 70 / 100
    elif age > 59:
        amount = ticket * 50 / 100
    else:
        amount = ticket

    total = total + amount

print("Total Amount =", total)