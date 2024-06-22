import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['nepal', 'pokhara', 'bajhang', "kathmandu", 'illam', "mustang"]

end_of_game = False

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

display = []

for _ in word_list:
    display += "_"
        

while not end_of_game:
    guess = input("Enter your guess letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win.")


    print(stages[lives])