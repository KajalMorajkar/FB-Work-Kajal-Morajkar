import random
userId=input("Enter user id :")
password=input("Enter password :")
if userId=="admin" and password=="Goal@2027":
    captch=random.randint(1000,9999)
    print(f"Your Captcha={captch}")
    chuser=int(input("Enter the Captcha=>"))
    if chuser==captch:
        print("User Login Successfully...")
    else:
        print("Invalid Captcha...")
else:
    print("User is Invalid")