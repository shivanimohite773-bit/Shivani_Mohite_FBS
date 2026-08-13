num = int(input("Enter a 3 digit number: "))
if(num<100 or num>999):

    print(f'Please enter a 3 digit number.')

else:

    if(num//100 == num%10):
        print(f'{num} number is palindrome.')

    else:
        print(f'{num} number is not a palindrome.')
