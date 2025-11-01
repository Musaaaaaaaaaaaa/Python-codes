##: Moosa Shehzad Abbasi
##: U37033529
##: Trivia Game –- Questions Class (15 pts) -- Trivia Questions (20 pts) -- Driver Program (25 pts)



# questions_module.py
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
        Questions("How many days are in a lunar year?", "354", "365", "243", "379", 1),
        Questions("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2),
        Questions("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", 4),
        Questions("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3),
        Questions("Which of these Winnie the Pooh characters is a donkey?", "Pooh", "Eeyore", "Piglet", "Kanga", 2),
        Questions("What is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", 4),
        Questions("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", 1),
        Questions("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", 3),
        Questions("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", 2),
        Questions("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", 4),
        
    ]

    return questions_list


# trivia_game.py

def play_trivia_game(questions):
    num_questions = len(questions)
    if num_questions % 2 != 0:
        print("Error: The total number of questions must be even.")
        return

    half_questions = num_questions // 2
    player1_score = 0
    player2_score = 0

    for i in range(half_questions):
        print(f"\nQuestion for the first player:")
        print(questions[i])
        player1_answer = int(input("Enter your solution (a number between 1 and 4): "))
        if player1_answer == questions[i].correct_answer:
            print("That is the correct answer.")
            player1_score += 1
        else:
            print(f"That is incorrect. The correct answer is {questions[i].correct_answer}")

        print(f"\nQuestion for the second player:")
        print(questions[i + half_questions])
        player2_answer = int(input("Enter your solution (a number between 1 and 4): "))
        if player2_answer == questions[i + half_questions].correct_answer:
            print("That is the correct answer.")
            player2_score += 1
        else:
            print(f"That is incorrect. The correct answer is {questions[i + half_questions].correct_answer}")

    print(f"The first player earned {player1_score} points.")
    print(f"The second player earned {player2_score} points.")

    if player1_score > player2_score:
        print("The first player wins the game.")
    elif player2_score > player1_score:
        print("The second player wins the game.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    trivia_questions = generate_questions()
    play_trivia_game(trivia_questions)
