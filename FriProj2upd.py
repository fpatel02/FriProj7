import random  # Importing the random module to use random number generation

# Greeting the user
print("Welcome to the Powerball Number Generator!")
print("This program will generate 5 random numbers between 1 and 69, and 1 Powerball number between 1 and 26.")

# Generating 5 random numbers between 1 and 69
powerball_numbers = []  # Creating an empty list to store the numbers
for _ in range(5):  # Looping 5 times to generate 5 numbers
    number = random.randint(1, 69)  # Generating a random number between 1 and 69
    powerball_numbers.append(number)  # Adding the generated number to the list

# Generating the Powerball number between 1 and 26
powerball_number = random.randint(1, 26)  # Generating a random Powerball number

# Formatting the output with spaces
output = "   ".join(map(str, powerball_numbers)) + "   " + str(powerball_number)  # Joining numbers with spaces

# Displaying the generated numbers
print("\nYour Powerball numbers are:")
print(output)  # Printing the formatted Powerball numbers

# Farewell message
print("\nThank you for using the Powerball Number Generator! Good luck!")
