#take input
p = int(input("Enter principle amount :"))
r = float(input("Enter rate of interest :"))
t = int(input("Enter time (year) :"))

# operation
ci = p * (1 + r / 100 ) **t * p

#display output

print(f'compound interest is: {ci}')