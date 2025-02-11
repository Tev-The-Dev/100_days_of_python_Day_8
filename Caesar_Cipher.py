alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for letter in original_text:
        if letter == " ":
            encrypted_text += " "
            continue
        position = alphabet.index(letter)
        if position + shift_amount > 25:
            new_position = position + shift_amount - 26
        else:
            new_position = position + shift_amount
        encrypted_letter = alphabet[new_position]
        encrypted_text += encrypted_letter
    print(encrypted_text)
def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter == " ":
            decrypted_text += " "
            continue
        position = alphabet.index(letter)
        if position - shift_amount < 0:
            new_position = position - shift_amount + 26
        else:
            new_position = position - shift_amount
        decrypted_letter = alphabet[new_position]
        decrypted_text += decrypted_letter
    print(decrypted_text)


def caesar(original_text, shift_amount, direct):
    if direct == "encode":
        encrypt(original_text, shift_amount)
    elif direct == "decode":
        decrypt(original_text, shift_amount)



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction != 'encode' and direction != 'decode':
    print("Sorry, we don't understand.")
    exit()
else:
    text = input("Type the Caesar ciphered message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text = text, shift_amount = shift, direct= direction)

#TODO-1: Create a function called 'encrypt' that takes the originial_text and shift_amount as 2 inputs

#TODO-2: Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text

#TODO-4: What happens if you tro to shift z forwards by 9? Can you fix the code?

#TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message
