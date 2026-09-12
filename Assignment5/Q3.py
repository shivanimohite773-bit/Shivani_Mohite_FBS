n = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost per passenger: "))

total = 0

for i in range(1, n + 1):
    age = int(input("Enter age of passenger " + str(i) + ": "))

    if age < 12:
        ticket = cost - (cost * 30 / 100)
        print("30% discount")

    elif age > 59:
        ticket = cost - (cost * 50 / 100)
        print("50% discount")

    else:
        ticket = cost
        print("No discount")

    total = total + ticket

print("Total ticket amount =", total)