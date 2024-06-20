year = int(input("ENter a year:"))

if year % 4 == 0 or year % 100 != 0 and year % 4 == 0 and year % 400 == 20:
    print("Yes")
else:
    print("no")

