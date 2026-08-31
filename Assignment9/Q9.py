def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)


m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

result = power(m, n)

print(m, "to the power", n, "=", result)