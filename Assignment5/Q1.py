correct_id = "admin"
correct_password = "1234"

for i in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect User ID or Password")

else:
    print("You have exceeded 3 attempts. Program terminated.")