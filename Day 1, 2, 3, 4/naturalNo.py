requiredNumber = int(input("Enter a number? "))

# # Print natural numbers upto n.
# for i in range(1, requiredNumber):
#     print(i)

# # Print reverse natural numbers from n to 1.
# for j in range (requiredNumber, 0, -1):
#     print(j)

# # table of the number
# for k in range(1, 11):
#     product = requiredNumber * k
# print(f"{requiredNumber} * {k} = {product}")

# # Sum upto n terms
# for l in range(1, requiredNumber):
#     sum = (requiredNumber * (requiredNumber + 1))/2
# print(f"sum of {requiredNumber} is {sum}.")

# # Factors of a number
for m in range(1, requiredNumber+1):
    if requiredNumber % m == 0:
        print(f"{m} is a factor of that number.")
    