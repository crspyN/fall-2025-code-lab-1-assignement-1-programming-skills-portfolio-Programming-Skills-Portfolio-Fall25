def capital_quiz():
    # Dictionary of European countries and their capitals
    questions = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Poland": "Warsaw",
        "Greece": "Athens",
        "Portugal": "Lisbon",
        "Sweden": "Stockholm",
        "Netherlands": "Amsterdam",
        "Austria": "Vienna"
    }
    
    score = 0
    total = len(questions)
    
    print("Welcome to the European Capitals Quiz!")
    print(f"Answer {total} questions. Good luck!\n")
    
    for i, (country, capital) in enumerate(questions.items(), 1):
        user_answer = input(f"Question {i}: What is the capital of {country}? ").strip()
        
        # Compare answers ignoring capitalization
        if user_answer.lower() == capital.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {capital}.\n")
    
    # Display final results
    print(f"Quiz Complete! Your score: {score}/{total}")
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")

# Run the quiz
if __name__ == "__main__":
    capital_quiz()