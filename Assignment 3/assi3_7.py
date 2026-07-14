correct_userId = "admin"
correct_password = "1234"

userId = input("Enter userId : ")
password = input("Enter password : ")

if userId == correct_userId:
    if password == correct_password:
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect User ID")