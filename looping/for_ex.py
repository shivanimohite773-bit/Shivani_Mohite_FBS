a = int(input("Enter the start number: "))
x = int(input("Enter the last number:"))
for val in range(a,x+1):
    if val%2!=0:
         print(val)