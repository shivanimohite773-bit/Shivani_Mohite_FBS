start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):
    temp = num
    total = 0
    digits = 0

    # Count number of digits
    while temp > 0:
        digits = digits + 1
        temp = temp // 10

    temp = num

    # Calculate sum of powers of digits
    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print(num)