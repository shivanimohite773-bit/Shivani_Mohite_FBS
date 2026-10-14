n = 21

# First row
print("*" * n)

# Middle 10 stars
for i in range(10):
    spaces = round((n - 1) * (9 - i) / 9)
    print(" " * spaces + "*")

# Last row
print("*" * n)