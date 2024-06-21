# Greated between 2 numbers

numberOne = int(input("Enter your first number: "))
numberTwo = int(input("Enter your second number: "))

if numberOne > numberTwo:
    print(f"Number {numberOne} is greatest.")
elif numberOne == numberTwo:
    print("They are equal.")
else:
    print(f"Number {numberTwo} is greatest.")
