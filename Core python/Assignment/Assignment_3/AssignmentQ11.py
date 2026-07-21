# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total = 0

# Person 1
age = int(input("Enter age of Person 1: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    ticket = ticket - (ticket * 30 / 100)
elif age > 59:
    ticket = ticket - (ticket * 50 / 100)
else:
    total = total + ticket

# Person 2
age = int(input("Enter age of Person 2: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    ticket = ticket - (ticket * 30 / 100)
elif age > 59:
    ticket = ticket - (ticket * 50 / 100)
else:
    total = total + ticket

# Person 3
age = int(input("Enter age of Person 3: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    ticket = ticket - (ticket * 30 / 100)
elif age > 59:
    ticket = ticket - (ticket * 50 / 100)
else:
    total = total + ticket

# Person 4
age = int(input("Enter age of Person 4: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    ticket = ticket - (ticket * 30 / 100)
elif age > 59:
    ticket = ticket - (ticket * 50 / 100)
else:
    total = total + ticket

# Person 5
age = int(input("Enter age of Person 5: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    ticket = ticket - (ticket * 30 / 100)
elif age > 59:
    ticket = ticket - (ticket * 50 / 100)
else:
    total = total + ticket

print("Total Ticket Amount =", total)