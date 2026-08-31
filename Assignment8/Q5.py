def even():
    n = int(input("Enter n : "))
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum = sum + i
   
    print(f"Sum of odd numbers = {sum}")
even()