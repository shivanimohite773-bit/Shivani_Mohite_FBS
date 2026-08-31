def reverse(num, rev=0):
    if num == 0:
        return rev
    else:
        digit = num % 10
        return reverse(num // 10, rev * 10 + digit)


num = int(input("Enter a number: "))

result = reverse(num)

print("Reverse number =", result)