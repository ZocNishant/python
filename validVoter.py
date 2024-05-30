name = str(input("Enter your name? "))

age = int(input("Enter your age? "))

if age >= 18 and age < 100:
    print(f"{name}, you're a valid voter at this age of {age}.")
elif age < 18 and age > 0:
    print(f"{name}, you're not a valid voter at this age of {age}.")
else:
    print(f"{name}, please enter a valid age.")