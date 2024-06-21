import random

nameInput = input("Give me the names of people with you: ")
name = nameInput.split(', ')

lengthOfTheList = len(name)

randomNumber = random.randint(0, lengthOfTheList)

print(f'{name[randomNumber]} is paying todays bill. Hehohahaha')


