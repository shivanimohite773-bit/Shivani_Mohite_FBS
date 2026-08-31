def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def sum(n):
    if n == 0:
        return 0
    else:
        return fact(n) + sum(n - 1)


n = int(input("Enter n: "))

res=fact(n)
result = sum(n)

print(f'factorial : {res}')
print(f"Sum of series = {result}")