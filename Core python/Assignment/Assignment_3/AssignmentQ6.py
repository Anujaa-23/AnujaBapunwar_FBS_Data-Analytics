# Write a program to calculate profit or loss.

cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))

if sp > cp:
    print("Profit")
elif cp > sp:
    print("Loss")
else:
    print("No Profit No Loss")