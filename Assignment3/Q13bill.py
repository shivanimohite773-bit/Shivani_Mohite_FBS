units = int(input("Enter electricity unit: "))

if(units <= 50):
    bill = units * 0.50
elif(units <= 150):
    bill = (units*0.50) + (units-50) * 0.75
elif(units <= 250):
    bill = (units*0.50) + (units*0.75) + ((units-50) * 1.20)
else:
    bill = (units*0.50) + (units*0.75) + (units*1.20) + ((units-50) * 1.50)

surcharge = bill * 20 /100
total_bill = bill + surcharge

print(f"Electricity bill= {bill}")
print(f'Surcharge = {surcharge}')
print(f'Total_bill={total_bill}')