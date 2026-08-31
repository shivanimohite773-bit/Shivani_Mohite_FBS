def sum_digits(num):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return digit + sum_digits(num // 10)


num = int(input("Enter a number: "))

result = sum_digits(num)

print("Sum of digits =", result)