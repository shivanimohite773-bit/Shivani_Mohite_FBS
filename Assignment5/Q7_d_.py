a = int(input("Enter a: "))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("S =", sum)