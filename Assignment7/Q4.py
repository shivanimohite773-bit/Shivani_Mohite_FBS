n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")

    for j in range(i):
        print(i + j, end=" ")

    for j in range(i - 2, -1, -1):
        print(i + j, end=" ")

    print()