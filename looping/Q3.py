num = int(input("Enter number:"))

while (num > 0):
    digit = num % 10  # get last digit
    print(digit)
    num = num // 10  #remove last digit
