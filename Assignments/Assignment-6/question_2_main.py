from question_2_trivia import Trivia
from question_2_player import player1, player2


game = Trivia(player1, player2)
game.start_the_game()

winner = Trivia.evaluate_winner(game)

print(winner)
