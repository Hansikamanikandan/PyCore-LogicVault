m1 = float(input("Enter mark1: "))
m2 = float(input("Enter mark2: "))
m3 = float(input("Enter mark3: "))
m4 = float(input("Enter mark4: "))
m5 = float(input("Enter mark5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("The average marks are:", average)
print("The total marks are:", total)

if average >= 90:
    print("Your grade is: O")
elif average >= 80:
    print("Your grade is: A+")
elif average >= 70:
    print("Your grade is: A")
elif average >= 55:
    print("Your grade is: B+")
elif average >= 50:
    print("Your grade is: C")
else:
    print("You are fail")
