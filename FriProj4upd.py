# Quiz Bowl

# Defining a dictionary with trivia questions and their answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest mammal in the world?": "Blue Whale",
    "What year did the Titanic sink?": "1912"
}

# Starting the quiz
print("Welcome to the Trivia Quiz Bowl!")
print("You will be asked 5 trivia questions. Let's see how many you can answer correctly!")

# Looping through the dictionary items
for question, correct_answer in trivia_questions.items():
    print(f"\nQuestion: {question}")  # Display the question
    user_answer = input("Your answer: ").strip()  # Prompt the user for their answer

    # Checking the user's answer against the correct answer
    if user_answer.lower() == correct_answer.lower():  # Case-insensitive comparison
        print("Correct! Well done!")  # Feedback for a correct answer
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")  # Feedback for a wrong answer

# Ending the quiz
print("\nThank you for playing the Trivia Quiz Bowl! Goodbye!")  # Farewell message
