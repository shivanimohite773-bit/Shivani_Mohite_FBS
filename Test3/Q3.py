'''3. Write a program to accept basic salary of n emp. (n should be
accepted from user). If basic salary is below 20000 then
da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
hra=20%. Based on this calculate the total salary of each emp
and also total salary of all emp.'''

n = int(input("Enter number of employees: "))

total_salary = 0

i = 1

while i <= n:
    basic = float(input("Enter basic salary: "))

    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra

    print("Employee", i)
    print("Basic Salary =", basic)
    print("DA =", da)
    print("TA =", ta)
    print("HRA =", hra)
    print("Total Salary =", salary)

    total_salary = total_salary + salary

    i = i + 1

print("Total Salary of all employees =", total_salary)