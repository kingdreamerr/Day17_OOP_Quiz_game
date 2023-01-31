class QuizBrain:
     def __init__(self, inputs):
        self.question_number = 0
        self.question_list = inputs
        self.score = 0
        
     def still_has_questions(self):
        length = len(self.question_list) - 1
        return length > self.question_number