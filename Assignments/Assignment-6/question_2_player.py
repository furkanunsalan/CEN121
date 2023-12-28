class Player:
    def __init__(self, name, player_no, score=0):
        self.name = name
        self.player_no = player_no
        self.score = score
    
    def change_score(self, points):
        self.score += points
        