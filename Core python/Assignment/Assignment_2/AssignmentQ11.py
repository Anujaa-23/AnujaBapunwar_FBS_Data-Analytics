# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input("Enter the amount: "))

# Calculate notes
note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

note5 = amount // 5
amount = amount % 5

note2 = amount // 2
amount = amount % 2

note1 = amount

print("500 Notes =", note500)
print("200 Notes =", note200)
print("100 Notes =", note100)
print("50 Notes =", note50)
print("20 Notes =", note20)
print("10 Notes =", note10)
print("5 Notes =", note5)
print("2 Notes =", note2)
print("1 Notes =", note1)