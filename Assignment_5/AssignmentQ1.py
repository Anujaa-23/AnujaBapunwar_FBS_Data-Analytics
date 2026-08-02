userid = "admin"
password = "1234"

count = 1

while count <= 3:
    u = input("Enter User ID: ")
    p = input("Enter Password: ")

    if u == userid and p == password:
        print("Login Successful")
        break
    else:
        print("Wrong User ID or Password")
        count = count + 1

if count > 3:
    print("Program Terminated")