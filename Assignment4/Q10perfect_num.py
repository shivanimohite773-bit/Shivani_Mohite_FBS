num = int(input("Enter number:"))
sum = 0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i

if(sum == num):
    print("Given number is perfect number.")
else:
    print("Given number is not perfect number.")