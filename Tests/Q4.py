# Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)


area = int(input("Enter area of one wall: "))
interior_cost = int(input("Enter cost of interior wall: "))
exterior_cost = int(input("Enter cost of exterior wall: "))

interior_total = area * 7 * interior_cost
exterior_total = area * 6 * exterior_cost

total_cost = interior_total + exterior_total 

print(f'interior printing cost{interior_total}')
print(f'exterior printing cost{exterior_total}')
print(f'total printing cost{total_cost}')