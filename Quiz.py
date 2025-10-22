# Simple Quiz Game
# Concepts: Dictionary, Loop, Conditionals

print("🧠 Welcome to the Python Quiz Game! 🧠")
print("Answer the following multiple-choice questions.\n")

# Questions stored in a dictionary
quiz = {
    "1. What is the keyword to define a function in Python?": {
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    "2. Which of the following is used to take input from the user?": {
        "options": ["A. input()", "B. get()", "C. scanf()", "D. read()"],
        "answer": "A"
    },
    "3. What is the correct file extension for Python files?": {
        "options": ["A. .pt", "B. .pyt", "C. .py", "D. .pyth"],
        "answer": "C"
    },
    "4. Which data type is immutable in Python?": {
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    "5. What will 3 ** 2 return?": {
        "options": ["A. 6", "B. 9", "C. 8", "D. Error"],
        "answer": "B"
    }
}

# Initialize score
score = 0

# Loop through all questions
for question, data in quiz.items():
    print(question)
    for option in data["options"]:
        print(option)
    
    answer = input("Your answer (A/B/C/D): ").upper()

    if answer == data["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {data['answer']}\n")

# Display final score
print("🎯 Quiz Completed!")
print(f"Your Final Score: {score} / {len(quiz)}")

# Simple performance feedback
if score == len(quiz):
    print("🏆 Excellent! You're a Python Pro!")
elif score >= 3:
    print("👍 Good job! Keep practicing.")
else:
    print("📘 Keep learning — you’ll improve soon!")
