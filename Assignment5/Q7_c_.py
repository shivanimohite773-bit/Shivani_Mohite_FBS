n = int(input("Enter n: "))

sum = 0
term = 1

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)