import random

print("Welcome to the Rock, Paper, Scissors game: ")

usersGuess = int(input("Enter one of 0,1 or 2: "))
print(f'Your guess is {usersGuess}')

computersGuess = random.randint(0, 2)
print(f'The Computers guess is {computersGuess}')

if usersGuess == computersGuess or usersGuess > 2 or usersGuess < 0:
    print("Match is draw.")
elif usersGuess == 0 and computersGuess == 2:
    print("Rock Wins.")
elif usersGuess == 1 and computersGuess == 0:
    print("Paper Wins")
elif usersGuess == 2 and computersGuess == 1:
    print("Scissors Wins")
else:
    print("You lose.")
    

