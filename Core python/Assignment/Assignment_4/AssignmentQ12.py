# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

n = int(input("Enter a number: "))

temp = n
count = len(str(n))
total = 0

while n>0:
    d= n % 10
    total= total+ (d** count)
    n= n // 10

if total== temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")