#take input
p = int(input("Enter principle amount :"))
r = float(input("Enter rate of interest :"))
t = int(input("Enter time (year) :"))

# operation
si = p * r * t /100

#display output

print(f'Simple interest is: {si}')