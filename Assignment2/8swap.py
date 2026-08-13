a = int(input('Enter the first number: '))
b = int(input('Enter the second number: ')) 

print(f"before swapping :")
print(f"a = {a}")
print(f"b = {b}")

temp = b
b = a
a = temp 

print(f"after swapping") 
print(f'a = {a}')
print(f'b = {b}')
