# trivia_game.py

class Questions:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    def __str__(self):
        return f"{self.question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}\n"

def generate_questions():
    questions_list = [
        Questions("What is the capital of France?", "Paris", "Berlin", "London", "Madrid", 1),
        Questions("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2),
        # Add more questions here...
        Questions("What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2),
        Questions("What is the currency of Japan?", "Yen", "Won", "Dollar", "Euro", 1),
        # Add more questions here...
    ]

    return questions_list

def play_trivia_game(questions):
    num_questions = len(questions)
    if num_questions % 2 != 0:
        print("Error: The total number of questions must be even.")
        return

    half_questions = num_questions // 2
    player1_score = 0
    player2_score = 0

    for i in range(half_questions):
        print(f"\nQuestion {i + 1} - Player 1's Turn:")
        print(questions[i])
        player1_answer = int(input("Enter your answer (1, 2, 3, or 4): "))
        if player1_answer == questions[i].correct_answer:
            player1_score += 1

        print(f"\nQuestion {i + 1} - Player 2's Turn:")
        print(questions[i + half_questions])
        player2_answer = int(input("Enter your answer (1, 2, 3, or 4): "))
        if player2_answer == questions[i + half_questions].correct_answer:
            player2_score += 1

    print("\nGame Over! Results:")
    print(f"Player 1's Score: {player1_score}")
    print(f"Player 2's Score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 Wins!")
    elif player2_score > player1_score:
        print("Player 2 Wins!")
    else:
        print("It's a Tie!")

if __name__ == "__main__":
    trivia_questions = generate_questions()
    play_trivia_game(trivia_questions)
