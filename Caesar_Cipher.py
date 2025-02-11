alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for letter in original_text:
        if not letter.isalpha():
            encrypted_text += letter
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
        if not letter.isalpha():
            decrypted_text += letter
            continue
        position = alphabet.index(letter)
        if position - shift_amount < 0:
            new_position = position - shift_amount + 26
        else:
            new_position = position - shift_amount
        decrypted_letter = alphabet[new_position]
        decrypted_text += decrypted_letter
    print(decrypted_text)


def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        encrypt(original_text, shift_amount)
    elif encode_or_decode == "decode":
        decrypt(original_text, shift_amount)



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction != 'encode' and direction != 'decode':
    print("Sorry, we don't understand.")
    exit()
else:
    text = input("Type the Caesar ciphered message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text = text, shift_amount = shift, encode_or_decode= direction)

