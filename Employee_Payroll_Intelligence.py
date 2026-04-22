i = int(input("Enter the salary of an employee: "))
n = int(input("Enter number of absence of an employee: "))

if n > 5:
    d = n * 500
    print("The detected amount will be:", d)
    print("Salary after detection will be:", i - d)
else:
    print("Salary of the employee:", i)
