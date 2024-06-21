listInputFromUser = input("Enter your desigred numbers in the list: ").split()


for n in range(0, len(listInputFromUser)):
    listInputFromUser[n] = int(listInputFromUser[n])
    

highestNumber = 0
for userInput in listInputFromUser:
    if userInput > highestNumber:
        highestNumber = userInput

print(f'The highest score is {highestNumber}')