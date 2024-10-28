# Mad Libs Generator

# Collecting user inputs
large_object = input("Enter a large object: ")  # Prompt user for a large object
large_objects_plural = input("Enter a plural form of a large object: ")  # Prompt for plural large objects
adjective = input("Enter an adjective: ")  # Prompt for an adjective
body_part = input("Enter a body part: ")  # Prompt for a body part
restaurant = input("Enter a restaurant: ")  # Prompt for a restaurant name
first_food = input("Enter a type of food: ")  # Prompt for the first food
second_food = input("Enter another type of food: ")  # Prompt for the second food

# Creating the Mad Lib story using formatted strings
mad_lib_story = (
    f"I’ve had a very {adjective} day.\n"
    f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n"
    f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n"
    f"But the waiter brought me {second_food}, which I was not hungry for.\n"
    f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."
)

# Displaying the completed Mad Lib story
print("\nHere's your Mad Lib:\n")
print(mad_lib_story)  # Print the final Mad Lib story
