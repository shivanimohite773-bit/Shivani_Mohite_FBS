num = int(input('Enter number: '))

if(num <= 0):
    print(f'{num} is a less than or equal to zero.')
elif(num <= 50):
    print(f'{num} is from 1 to 50.')
elif(num <= 100):
    print(f'{num} is from 51 to 100.')
elif(num <= 150):
    print(f'{num} is from 101 to 150.')
elif(num <= 250):
    print(f'{num} is from 151 to 250.')
else:
    print(f'{num} is greater than 250.')