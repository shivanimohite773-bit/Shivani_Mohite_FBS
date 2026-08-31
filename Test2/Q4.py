l = float(input("Enter length of room: "))
b = float(input("Enter breadth of room: "))
h = float(input("Enter height of room: "))
rate = float(input("Enter painting cost per sq.m: "))

area = 2 * (l + b) * h
cost = area * rate

print("Total cost of painting =", cost)