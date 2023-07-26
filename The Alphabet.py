# Create a string of all the letters in the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Loop over each letter and print the message
for letter in alphabet:
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
