num = int(input("Enter number:"))
count = len(str(num))
temp = num
sum = 0
while (num > 0):
    d = num % 10
    num = num//10
    sum = sum + (d ** count)
if(temp==sum):
    print(f'{temp} is Armstrong number.')
else:
    print(f'{temp} is not Armstrong number.')
