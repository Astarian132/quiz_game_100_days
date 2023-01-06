from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for i in question_data:
  question_bank.append(Question(i['text'],i['answer']))

new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_questions():
  new_quiz.next_question()

print(f"\n \nNo more questions, Your score was {new_quiz.score} out of {len(new_quiz.question_list)}")