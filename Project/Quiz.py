# Quiz data
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["a) Mumbai", "b) Delhi", "c) Kolkata", "d) Chennai"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Venus", "c) Mars", "d) Jupiter"],
        "answer": "c"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["a) 10", "b) 11", "c) 12", "d) 13"],
        "answer": "c"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["a) HTML", "b) Python", "c) C", "d) Java"],
        "answer": "a"
    }
]

score = 0  # Global score counter

def ask_question(index):
    global score
    if index == len(questions):
        print("\n🎉 Quiz Complete!")
        print(f"✅ Your Final Score: {score}/{len(questions)}")
        return

    q = questions[index]
    print(f"\nQ{index + 1}: {q['question']}")
    for option in q["options"]:
        print(option)

    answer = input("Your answer (a/b/c/d): ").lower()

    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was '{q['answer']}'")

    ask_question(index + 1)  # Recursive call to the next question

# Start the quiz
print("📚 Welcome to the Python Quiz!")
ask_question(0)
