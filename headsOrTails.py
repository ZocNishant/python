import random

print("Welcome to Heads or Tails. That is if you don't have a real coin and want a virtual one.")
randomNumber = random.randint(0,1)

if randomNumber == 0:
    print("Wow! Lucky you. It is a Head.")
else:
    print("It is a Tail.")

