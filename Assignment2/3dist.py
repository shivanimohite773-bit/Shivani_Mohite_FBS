# input

feet = float(input("Enter the distance in feet: "))
inches = float(input("Enter the distance in inches: "))

#operation

total_inches = (feet * 12) + inches 

meters = total_inches * 0.0254

centimeter = meters * 100

#display output
print(f"distance in Meter: {meters} ")
print(f"distance in centimeter: {centimeter}")