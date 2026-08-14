# Write a program to accept distance in km and convert it into meters and centimeters both


km = float(input("Enter distance in kilometer: "))

meter = km * 1000
centimeter = km * 100000

print(f'Distance in meter : {meter}')
print(f'Distance in centimeter: {centimeter}')