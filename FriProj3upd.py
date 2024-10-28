import random  # Importing the random module to generate random numbers

# Greeting the user
print("Welcome to the Number Guessing Game!")
play_game = input("Do you want to play? (yes/no): ").strip().lower()  # Asking the user if they want to play, converting input to lowercase

# If the user does not want to play, exit the game
if play_game != 'yes':
    print("Thank you for your time! Goodbye!")  # Farewell message for quitting
else:
    while True:  # Start a loop to play the game
        number_to_guess = random.randint(1, 10)  # Generate a random number between 1 and 10
        attempts = 0  # Initialize the number of attempts made by the user

        print("\nI've chosen a number between 1 and 10. Try to guess it!")
        while True:  # Loop for the guessing part of the game
            guess = input("Enter your guess (or type 'quit' to exit): ")  # Prompt user for their guess

            if guess.lower() == 'quit':  # Check if the user wants to quit
                print("Thank you for playing! Goodbye!")  # Farewell message for quitting
                break  # Exit the guessing loop

            attempts += 1  # Increment the attempt count
            try:
                guess = int(guess)  # Convert the user's guess to an integer
            except ValueError:  # Handle the case where the input is not a number
                print("Please enter a valid number.")  # Prompt user for valid input
                continue  # Go to the next iteration of the loop

            if guess < number_to_guess:  # Check if the guess is too low
                print("Too low! Try again.")  # Inform the user their guess was too low
            elif guess > number_to_guess:  # Check if the guess is too high
                print("Too high! Try again.")  # Inform the user their guess was too high
            else:  # The guess is correct
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")  # Congratulate the user
                break  # Exit the guessing loop

        if guess.lower() == 'quit':  # If the user quit the guessing loop
            break  # Exit the main game loop

    print("Thank you for playing! Goodbye!")  # Farewell message when the game ends
