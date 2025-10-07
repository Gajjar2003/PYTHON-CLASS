

def quiz_game():
    print("🎯 Welcome to the Quiz Game!\n")

  
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["A. Python", "B. Java", "C. JavaScript", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
            "answer": "B"
        },
        {
            "question": "Who developed Python programming language?",
            "options": ["A. Elon Musk", "B. Bill Gates", "C. Guido van Rossum", "D. Mark Zuckerberg"],
            "answer": "C"
        }
    ]

    score = 0


    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

 
    print("🎉 Quiz Over!")
    print(f"Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! Perfect score!")
    elif score >= len(questions)//2:
        print("👍 Good job!")
    else:
        print("💪 Keep practicing!\n")


if __name__ == "__main__":
    quiz_game()
