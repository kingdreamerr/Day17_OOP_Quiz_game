from question_bank import q_bank
from quiz_brain import QuizBrain

game = QuizBrain(q_bank)
game.next_question()
score = 0
while game.still_has_questions():
    game.next_question()

print("You have completed the quiz")
print(f"Your final score is: {game.score}/{game.question_number}")



