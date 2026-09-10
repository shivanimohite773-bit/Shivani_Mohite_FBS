num = int(input('Enter number: '))

if(num > 0):

    if(num <= 50):
         print(f'{num} is from 1 to 50.')
    else:

        if(num <= 100):
             print(f'{num} is from 51 to 100.')
        else:

            if(num <= 150):
                 print(f'{num} is from 101 to 150.')
            else:

                if(num > 250):
                    print(f'{num} is from 151 to 250.')
                else:
                    print(f'{num} is greater than 250.')
                    
else:
    print(f'{num} is a less than or equal to zero.')