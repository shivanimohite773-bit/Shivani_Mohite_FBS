def cube_sum(num):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10

    return total


def check_armstrong(num):
    result = cube_sum(num)

    if result == num:
        print(num, "is an Armstrong Number")
    else:
        print(num, "is not an Armstrong Number")


num = int(input("Enter a number: "))
check_armstrong(num)