# # ....

# total_amount = 0
# age1 = int(input("Enter the age of first person="))
# tkp1 = float(input("Enter the price of 1st person="))
# if ( age1 < 12 ):
#     disco= tkp1*(30/100)
#     print(f"Passenger get discount of rs{disco}")
#     total_amount = total_amount + (tkp1 - disco)
# elif age1 > 59:
#     disco = tkp1 * (50/100)
#     print(f"Passenger get discount of rs {disco}")
#     total_amount = total_amount + (tkp1 - disco)
# else:
#     total_amount = total_amount + tkp1


total = 0

for i in range(1,5):
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)
    elif age > 59:
        amount = ticket - (ticket * 50 / 100)
    else:
        amount = ticket

    total = total + amount

print("Total ticket amount =", total)