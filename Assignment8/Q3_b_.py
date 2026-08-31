def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + factorial(i)
    return sum

n = int(input("Enter n: "))
result = sum_series(n)
print("Sum =", result)