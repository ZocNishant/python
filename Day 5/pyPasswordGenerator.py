import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the ZOC Password generator.")

howMantLetters = int(input("Enter the number of letters you want in you password: \n"))
howManySymbols = int(input("Enter the number of symbols you want in you password: \n"))
howManyNumbers = int(input("Enter the number of numbers you want in you password: \n"))

# simple
# password = ""

# for char in range(1, howMantLetters + 1):
#     password = random.choice(letters)


# for symbol in range(1, howManySymbols +1):
#     password = random.choice(symbols)

# for number in range(1, howManyNumbers + 1):
#     password = random.choice(numbers)

# print(password)

# Hard
passwordLst = []

for char in range(1, howMantLetters + 1):
    passwordLst.append(random.choice(letters))


for symbol in range(1, howManySymbols + 1):
    passwordLst += random.choice(symbols)

for number in range(1, howManyNumbers + 1):
    passwordLst += random.choice(numbers)

print(passwordLst)

random.shuffle(passwordLst)

pssd = ""
for eachChar in passwordLst:
    pssd += eachCharv

print(pssd)