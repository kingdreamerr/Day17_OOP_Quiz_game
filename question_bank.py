from question_model import Question
from data import question_data

q_bank = []
for obj in question_data:
    q_bank.append(Question(obj["text"], obj["answer"]))

