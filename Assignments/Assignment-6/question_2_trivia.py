from question_2_player import player1, player2
from question_2_questions import Question

question = Question()


class Trivia:
    def __init__(self, player1, player2, current_player=player1):
        self.player1 = player1
        self.player2 = player2
        self.current_player = current_player
    
    def change_turn(self):
        if self.current_player == player1:
            self.current_player = player2
        else:
            self.current_player = player1
    
    def start_the_game(self):
        for i in range(10):
            print()
            question.choose_question()
            
            print(f"{self.current_player.name}'s turn")
            print(question.question)
            print()
            
            for choice in question.options:
                print(choice)
            print()
            
            answer = input("Enter the answer phrase: ")
            
            if answer.lower() == question.answer:
                print("Correct Answer!")
                self.current_player.increase_score(1)
                self.change_turn()
            else:
                print(f"Incorrect Answer! The correct answer is {question.answer.upper()}")
                self.change_turn()
            
    def evaluate_winner(self):
        print()
        print(f"{player1.name}'s score: {player1.score}")
        print(f"{player2.name}'s score: {player2.score}")
        
        if player1.score > player2.score:
            return f"{player1.name} wins the game!"
        
        elif player1.score < player2.score:
            return f"{player2.name} wins the game!"
        else:
            return f"{player1.name} and {player2.name} are tied!"
            