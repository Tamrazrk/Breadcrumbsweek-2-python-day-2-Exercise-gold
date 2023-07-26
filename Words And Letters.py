# Ask the user for 7 words and store them in a list
words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

# Ask the user for a single character
letter = input("Enter a single character: ")

# Loop through the words list and print the index of the first appearance of the letter in each word
for word in words:
    if letter in word:
        index = word.index(letter)
        print(f"The index of '{letter}' in '{word}' is: {index}")
    else:
        print(f"'{letter}' does not exist in '{word}'.")
