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