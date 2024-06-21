getNumberToCheck = int(input("Enter the desigred number to be checked for odd or even: "))

if getNumberToCheck % 2 == 0:
    print(f'The given number {getNumberToCheck} seems to be even.')
else:
    print(f'The given number {getNumberToCheck} seems to be odd.')

print("Plese check more numbers.")