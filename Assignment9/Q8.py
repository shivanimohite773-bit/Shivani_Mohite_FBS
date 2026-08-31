def check_prime(num, i=2):
    if (num <= 1):
        return False
    elif (i * i > num):
        return True
    elif (num % i == 0):
        return False
    else:
        return check_prime(num, i + 1)


num = int(input("Enter a number: "))

if check_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")