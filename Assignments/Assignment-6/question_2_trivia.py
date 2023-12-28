from question_2_player import player1, player2
from question_2_questions import questions


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
        
    
    def ask_questions(self):
        for key in questions:
            print()
            print(f"{self.current_player.name}'s turn")
            print(key)
            print()
            
            for choice in questions[key][1]:
                print(choice)
            print()
                
            answer = input("Enter the answer phrase: ")
            
            if answer.lower() == questions[key][0]:
                print("Correct Answer!")
                self.current_player.change_score(1)
                self.change_turn()
                    
            else:
                print(f"Incorrect Answer! The correct answer is {questions[key][0].upper()}")
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
        
            