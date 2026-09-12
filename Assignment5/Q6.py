n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

while count < n:
    factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factors = factors + 1

    if factors == 2:
        print(num)
        count = count + 1

    num = num + 1