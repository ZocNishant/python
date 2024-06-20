# --------Syntax-----------

# if condition:
#     do this
# else:
#     do this

# .................................

# >
# <
# >=
# <=
# ==
# !=

# IF...ELSE

# print("OO-OO`--o Rollercoaster Ride.")
# height = int(input("Enter your height: "))

# if height >= 120:
#     print("Yes, you can ride the thing.")
# else:
#     print("Sorry, you can't ride the thing. Go back let the next person come through. Thanks.")

# NESTED IF ELSE

print("OO-OO`--o Rollercoaster Ride.")
height = int(input("Enter your height: "))

if height >= 120:
    print("Yes, you can ride the thing.")
    print("Let me get some more details from you so that I can give you the price of the ticket.")

    age = int(input("Enter your age: "))

    
    if age > 80 or age <= 120:
        print("Sorry, the ride is risky for you. Please go and have some rest in the lounge.")
    elif age >=25 or age < 80:
        print("Your total ticket price is 40$.")
    elif age >=18 or age < 25:
        print("The price of your ticket is 30$.")
    elif age < 18 or age > 10:
        print("The price of your ticket is 20$.")
    else:
        print("Sorry young one. You will play after some years okay. (●'◡'●)")
else:
    print("Sorry, you can't ride the thing. Go back let the next person come through. Thanks.")