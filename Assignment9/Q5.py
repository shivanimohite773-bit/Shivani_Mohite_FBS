def factorial(n):
    if(n == 0):
        return 0
    else:
        return n + factorial(n - 1)

num = int(input("Enter number: "))
res= factorial(num)
print(res)