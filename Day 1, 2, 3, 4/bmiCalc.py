print("Welcome to the BMI (Body Mass Index) Calculator.╰(*°▽°*)╯")

getWeight = float(input("Enter your weight in kilogram: "))
getHeight = float(input("Enter your height in meter: "))

bmi = getWeight / (getHeight ** 2)

if bmi > 16.5:
    print("Yes, nice.")
else:
    print("No")