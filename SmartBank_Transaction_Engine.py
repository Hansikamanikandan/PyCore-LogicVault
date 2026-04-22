n = int(input("Enter the initial balance: "))
print("Enter 1 for deposit and 2 for withdrawal")
c = int(input("Enter the type of transaction: "))

if c == 1:
    a = int(input("Enter amount to be deposited: "))

    if a > 1000:
        n = n + a
        print("Successfully deposited")
        print("Balance:", n)
    else:
        print("The deposit amount is not sufficient! It should be greater than 1000")

elif c == 2:
    b = int(input("Enter the amount to be withdrawal: "))
    d = n - b

    if d >= 1000:
        print("Successfully withdrawal")
        print("Balance:", d)
    else:
        print("The account balance is not sufficient! Minimum balance should be 1000")

else:
    print("Invalid transaction")
