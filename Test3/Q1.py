# 1. Write a program to print first n prime numbers

n = int(input("Enter n: "))

count = 0
num = 2

while count < n:
    i = 2
    temp = 0

    while i < num:
        if num % i == 0:
            temp = 1
            break
        i = i + 1

    if temp == 0:
        print(num)
        count = count + 1

    num = num + 1