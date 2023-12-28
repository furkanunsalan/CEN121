from question_2_trivia import Trivia, player1

game = Trivia(player1)
game.ask_questions()

winner = Trivia.evaluate_winner(game)
print(winner)
