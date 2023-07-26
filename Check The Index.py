names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask the user for their name
user_name = input("Enter your name: ")

# Find the index of the first occurrence of the user's name in the list
if user_name in names:
    index = names.index(user_name)
    print(f"The index of the first occurrence of {user_name} is: {index}")
else:
    print(f"{user_name} is not in the list.")
