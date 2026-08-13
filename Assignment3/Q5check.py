side1 = int(input("Enter the first side:"))
side2 = int(input("Enter the second side:"))
side3 = int(input("Enter the third side:"))

# Check if triangle is valid
if (side1 + side2 > side3 and
    side1 + side3 > side2 and
    side2 + side3 > side1):
    if (side1 == side2 == side3):
        print('The triangle is Equilateral.')
    elif(side1 == side2 or side1 == side3 or side2 == side3):
        print('The triangle is Isosceles.')
    else:
        print("The Triangle is Scalene.")
else:
    print("Invaild triangle.")
