# Colorful Text Functions 

# Defining functions for different text colors
def red(text):
    return f"\033[91m{text}\033[0m"  # Red color

def green(text):
    return f"\033[92m{text}\033[0m"  # Green color

def blue(text):
    return f"\033[94m{text}\033[0m"  # Blue color

def yellow(text):
    return f"\033[93m{text}\033[0m"  # Yellow color

def magenta(text):
    return f"\033[95m{text}\033[0m"  # Magenta color

# Main program
if __name__ == "__main__":
    # Displaying colored text using the defined functions
    print(red("This text is red!"))
    print(green("This text is green!"))
    print(blue("This text is blue!"))
    print(yellow("This text is yellow!"))
    print(magenta("This text is magenta!"))

    # User input for color selection
    color_choice = input("Choose a color (red, green, blue, yellow, magenta): ").strip().lower()  # Prompt user for color choice
    user_text = input("Enter the text you want to display: ")  # Prompt user for the text to display

    # Dictionary to map color choices to functions
    color_functions = {
        "red": red,
        "green": green,
        "blue": blue,
        "yellow": yellow,
        "magenta": magenta
    }

    # Checking if the user's color choice is valid and displaying the text
    if color_choice in color_functions:
        print(color_functions[color_choice](user_text))  # Call the corresponding function and print the colored text
    else:
        print("Invalid color choice! Please choose from red, green, blue, yellow, or magenta.")  # Error message for invalid input
