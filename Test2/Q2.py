num = int(input("Enter 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a == 2 * b and c == 2 * a:
    print("Yes, you have done it")
else:
    print("Please try next time")