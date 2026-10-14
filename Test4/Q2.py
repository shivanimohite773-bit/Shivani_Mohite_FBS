# 2. Write a program to find factorial of given number using recursion

def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter number:"))
result = fact(num)
print(f"factorial={result}")