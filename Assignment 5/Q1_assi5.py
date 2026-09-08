username = "admin"
password = "1234"

for i in range(3):
    u = input("Enter Username: ")
    p = input("Enter Password: ")

    if u == username and p == password:
        print("Login Successful")
        break
    else:
        print("Wrong Username or Password")

else:
    print("Account Blocked")