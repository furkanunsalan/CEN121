class Player:
    def __init__(self, name, player_no, score=0):
        self.name = name
        self.player_no = player_no
        self.score = score
    
    def change_score(self, points):
        self.score += points
        
player1_name = input("Enter name for Player-1: ")
player2_name = input("Enter name for Player-2: ")

player1 = Player(player1_name, 1)
player2 = Player(player2_name, 2)