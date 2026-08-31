def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** i
    return sum

n = int(input("Enter n: "))
result = sum_series(n)
print("Sum =", result)