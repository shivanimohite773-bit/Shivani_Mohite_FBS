##take input

days = int(input("Enter numbers of days: "))

#years
years = days // 365
days = days % 365

#weeks
weeks = days // 7
days = days % 7


print(f"years : {years}")
print(f"week : {weeks}")
print(f"days : {days}")