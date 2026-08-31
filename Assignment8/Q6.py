def fibonacci():
    n = int(input("Enter the number: "))

    a = 0
    b = 1

    for i in range(n):
        c = a + b
        print(c , end = ' ')
        a = b 
        b = c

fibonacci()