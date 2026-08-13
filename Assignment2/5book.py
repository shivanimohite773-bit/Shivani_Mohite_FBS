#input
cost_price = float(input("Enter the cost price of book :"))
discount = float(input("Enter discount :"))

#operation
Discount_amount = (cost_price * discount) / 100

selling_price = cost_price - Discount_amount

#display
print(f"The discount amount of book is : {Discount_amount}")
print(f"The selling price of book is : {selling_price}")