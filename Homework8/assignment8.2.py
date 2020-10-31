try:
    print("INTEGER DIVISIONS")
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print("Result of Division: " + str(a/b))
    print("CORRECT")

except (ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")

except(ValueError):
    print("Please enter Integer Only!")
