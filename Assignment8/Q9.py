def palindrome(num):
    temp = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if temp == reverse:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")


num = int(input("Enter a number: "))
palindrome(num)