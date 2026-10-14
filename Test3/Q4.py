'''4. Write a program to print pattern
10101
01010
10101
01010
10101'''

i = 1

while i <= 5:
    j = 1

    while j <= 5:
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")

        j = j + 1

    print()
    i = i + 1