# FriProj7

# Name: Fauram Patel
# Due Date: 27 October 2024
# Friday Project 7: Remake all previous Friday Project files using generative AI and gitHub

Notes on code:

FridayProj1upd:
        Input Collection:

        Each input() function prompts the user to enter a specific type of word. The results are stored in variables for later use in the story.
        large_object, large_objects_plural, adjective, body_part, restaurant, first_food, and second_food are variables that hold the user inputs.
    Creating the Mad Lib Story:

        A multiline formatted string (mad_lib_story) is created using f-strings. This allows for easy insertion of user inputs into the predefined story.
        The \n is used to add line breaks in the story for better readability.
    Displaying the Result:

        The final story is printed out with a  descriptive message to inform the user that their Mad Lib is ready.

FridayProj2upd:
    Importing the Random Module:

        import random: This imports the random module, which contains functions for generating random numbers.
    Greeting the User:

        print("Welcome to the Powerball Number Generator!"): Displays a welcome message to the user.
        print("This program will generate 5 random numbers between 1 and 69, and 1 Powerball number between 1 and 26."): Informs the user about what the program does.
    Generating Random Numbers:

        powerball_numbers = []: Initializes an empty list to store the first five random numbers.
        for _ in range(5): Creates a loop that iterates 5 times to generate 5 random numbers.
        number = random.randint(1, 69): Generates a random integer between 1 and 69 (inclusive).
        powerball_numbers.append(number): Adds the generated number to the powerball_numbers list.
    Generating the Powerball Number:

        powerball_number = random.randint(1, 26): Generates a random integer for the Powerball number between 1 and 26 (inclusive).
    Formatting the Output:

        output = " ".join(map(str, powerball_numbers)) + " " + str(powerball_number): Converts the numbers in the list to strings, joins them with three spaces, and appends the Powerball number with three spaces in between.
    Displaying the Generated Numbers:

        print("\nYour Powerball numbers are:"): Prints a message before showing the numbers.
        print(output): Outputs the formatted string containing the Powerball numbers.
    Farewell Message:

        print("\nThank you for using the Powerball Number Generator! Good luck!"): Displays a goodbye message to the user.

FridayProj3upd:
    Importing the Random Module:

        import random: This imports the random module to enable random number generation.
    Greeting the User:

        print("Welcome to the Number Guessing Game!"): Displays a welcome message to the user.
        play_game = input("Do you want to play? (yes/no): ").strip().lower(): Asks the user if they want to play, strips any extra spaces, and converts the input to lowercase for consistency.
    Checking User's Response:

        if play_game != 'yes':: Checks if the user's response is not 'yes'.
        print("Thank you for your time! Goodbye!"): Displays a farewell message if the user does not want to play.
    Starting the Game Loop:

        else:: If the user wants to play, we enter the game loop.
        while True:: Begins an infinite loop for playing the game.
        number_to_guess = random.randint(1, 10): Generates a random number between 1 and 10.
        attempts = 0: Initializes a counter for the number of attempts made by the user.
    Guessing Loop:

        print("\nI've chosen a number between 1 and 10. Try to guess it!"): Informs the user that the game has started.
        while True:: Begins another infinite loop for guessing the number.
        guess = input("Enter your guess (or type 'quit' to exit): "): Prompts the user to enter their guess.
    Handling Quit Option:

        if guess.lower() == 'quit':: Checks if the user wants to quit the game.
        print("Thank you for playing! Goodbye!"): Displays a farewell message for quitting.
        break: Exits the guessing loop.
    Counting Attempts and Validating Input:

        attempts += 1: Increments the attempt counter.
        try:: Starts a try-except block to handle errors.
        guess = int(guess): Converts the guess to an integer.
        except ValueError:: Catches any errors from invalid input.
        print("Please enter a valid number."): Prompts for valid input.
        continue: Skips to the next iteration of the loop.
    Checking the Guess:

        if guess < number_to_guess:: Checks if the guess is too low.
        print("Too low! Try again."): Informs the user to try again.
        elif guess > number_to_guess:: Checks if the guess is too high.
        print("Too high! Try again."): Informs the user to try again.
        else:: If the guess is correct.
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!"): Congratulates the user.
    Ending the Game:

        if guess.lower() == 'quit':: Checks if the user quit the guessing loop.
        break: Exits the main game loop.
        print("Thank you for playing! Goodbye!"): Displays a final farewell message.

FridayProj4upd:
    Defining the Dictionary:

        trivia_questions = {...}: This creates a dictionary where each key-value pair consists of a trivia question (key) and its corresponding answer (value).
    Starting the Quiz:

        print("Welcome to the Trivia Quiz Bowl!"): Displays a welcome message to the user.
        print("You will be asked 5 trivia questions. Let's see how many you can answer correctly!"): Informs the user about what to expect in the quiz.
    Looping Through Questions:

        for question, correct_answer in trivia_questions.items():: This loop iterates over each key-value pair in the dictionary, unpacking the question and its correct answer.
    Displaying the Question:

        print(f"\nQuestion: {question}"): Prints the current trivia question.
        user_answer = input("Your answer: ").strip(): Prompts the user for their answer and removes any leading or trailing whitespace.
    Checking the User's Answer:

        if user_answer.lower() == correct_answer.lower():: Compares the user's answer to the correct answer in a case-insensitive manner.
        print("Correct! Well done!"): Prints feedback for a correct answer.
        else:: Executes if the user's answer is incorrect.
        print(f"Wrong! The correct answer is: {correct_answer}"): Provides feedback and shows the correct answer.
    Ending the Quiz:

        print("\nThank you for playing the Trivia Quiz Bowl! Goodbye!"): Displays a farewell message to the user once all questions have been asked.

FridayProj5upd:
    Defining Functions for Colors:

        Each function (e.g., def red(text):) takes a string text as input.
        return f"\033[91m{text}\033[0m": The string is formatted with ANSI escape codes to change the text color.
        \033[91m: Sets the text color to red.
        \033[0m: Resets the color back to the default after the text.
    Main Program Execution:

        if __name__ == "__main__":: This checks if the script is being run directly (not imported as a module).
        print(red("This text is red!")): Calls the red function and prints the text in red color. This is repeated for each color function.
        User Input for Color Selection:

        color_choice = input("Choose a color (red, green, blue, yellow, magenta): ").strip().lower(): Prompts the user to choose a color, stripping whitespace and converting to lowercase for consistency.
        user_text = input("Enter the text you want to display: "): Prompts the user to input the text they wish to display.
    Mapping Color Choices to Functions:

        color_functions = {...}: This dictionary maps color names to their respective functions, allowing for easy lookup based on user input.
    Validating User Input:

        if color_choice in color_functions:: Checks if the user's choice is valid.
        print(color_functions[color_choice](user_text)): Calls the corresponding function and prints the colored text.
        else:: If the user's choice is invalid, it prints an error message.

FridayProj6upd:
    Class Definition: class BankAccount defines a class to manage bank accounts.
    __init__ Method: This method initializes a new bank account with an account number and sets the balance to zero.
    deposit Method: This method adds a specified amount to the balance. It checks if the amount is positive.
    withdraw Method: This method subtracts a specified amount from the balance if there are sufficient funds. It checks for positive amounts and available funds.
    check_balance Method: This method displays the current balance of the account.
    main Function: This function handles user input and interacts with the BankAccount class.
        It prompts the user for their account number and creates an account.
        It enters an indefinite loop, allowing users to choose options for depositing, withdrawing, checking their balance, or exiting.
        User inputs are processed, and appropriate methods are called based on their choices.
    Program Execution: The program starts by calling the main function.