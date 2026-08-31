def armstrong_sum(num):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return digit ** 3 + armstrong_sum(num // 10)


num = int(input("Enter a number: "))

result = armstrong_sum(num)

if result == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")