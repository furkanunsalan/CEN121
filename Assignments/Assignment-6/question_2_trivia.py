from question_2_player import Player

question = {
        "Q1": ["a", ["a", "b", "c", "d"]],
        "Q2": ["b", ["a", "b", "c", "d"]],
        "Q3": ["c", ["a", "b", "c", "d"]],
        "Q4": ["d", ["a", "b", "c", "d"]],
        #"Q5": ["a", ["a", "b", "c", "d"]],
        #"Q6": ["b", ["a", "b", "c", "d"]],
        #"Q7": ["c", ["a", "b", "c", "d"]],
        #"Q8": ["d", ["a", "b", "c", "d"]],
        #"Q9": ["a", ["a", "b", "c", "d"]],
        #"Q10": ["b", ["a", "b", "c", "d"]],
        }

player1 = Player("Player 1", 1)
player2 = Player("Player 2", 2)


class Trivia:
    def __init__(self, player):
        self.player = player
        
    
    def ask_questions(self):
        for key in question:
            print(f"{self.player.name}'s turn")
            print(key)
            
            for choice in question[key][1]:
                print(choice)
                
            answer = input("Enter your answer: ")
            
            if answer.lower() == question[key][0]:
                print("Correct!")
                if self.player.player_no == 1:
                    player1.change_score(1)
                    self.player = player2
                else:
                    player2.change_score(1)
                    self.player = player1
                    
            else:
                print("Incorrect!")
                if self.player.player_no == 1:
                    self.player = player2
                else:
                    self.player = player1
            
    def evaluate_winner(self):
        print(f"{player1.name}'s score: ")
        print(f"{player2.name}'s score: ")
        
        if player1.score > player2.score:
            return f"{player1.name} wins!"
        
        elif player1.score < player2.score:
            return f"{player2.name} wins!"
        else:
            return "Tie!"
            