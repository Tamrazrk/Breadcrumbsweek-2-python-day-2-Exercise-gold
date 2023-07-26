import random

total_games_won = 0
total_games_lost = 0

while True:
    # Ask the user to input a number from 1 to 9
    user_guess = input("Guess a number from 1 to 9 (enter 'q' to quit): ")

    # Check if the user wants to quit
    if user_guess.lower() == 'q':
        print("Exiting the game.")
        break

    # Generate a random number between 1 and 9
    random_number = random.randint(1, 9)

    # Check if the user's guess matches the random number
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            total_games_won += 1
            print("Winner! You guessed the correct number.")
        else:
            total_games_lost += 1
            print(f"Better luck next time. The correct number was {random_number}.")
    else:
        print("Invalid input. Please enter a number from 1 to 9 or 'q' to quit.")

# Display total games won and lost
print(f"\nTotal games won: {total_games_won}")
print(f"Total games lost: {total_games_lost}")
