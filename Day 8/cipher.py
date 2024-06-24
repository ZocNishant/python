alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(userInput, shiftingAmount):

    
    for letter in userInput:
        cipher_text = ""
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
        print(cipher_text)
        
 
def decrypt(cipherText, shiftingAmount):
    plaintext = ""
    for letter in cipherText:
        position = alphabet.index(letter)
        new_position = position - shiftingAmount
        plaintext += alphabet[new_position]
    print(f"The decoded message is {plaintext}")

encrypt(userInput=text, shiftingAmount=shift)

if direction == "encode":
    encrypt(plaintext=text, shiftingAmount=shift)
else:
    decrypt(cipherText=text, shiftingAmount=shift)