alphabet = "abcdefghijklmnopqrstuvwxyz"
shifted_message = ""

entered_sentence = input("Please enter your sentence:").lower()
shift = 5

for letter in entered_sentence:
    if letter in alphabet:
        position = alphabet.find(letter)
        new_position = (position + shift) % 26
        new_character = alphabet[new_position]
        shifted_message += new_character
    else:
        shifted_message += letter

print("The encrypted sentence is:", shifted_message)



    
