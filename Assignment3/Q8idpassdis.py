import random
userid = str(input("Enter userid: "))
password = int(input("Enter password: "))

if(userid == "shivanimohite" and password == 12093487):
    num =random.randint(1000,9999)
    print("Captacha:", num)


    print("Login successfully.")
else:
    print("Invaild userid and password.")