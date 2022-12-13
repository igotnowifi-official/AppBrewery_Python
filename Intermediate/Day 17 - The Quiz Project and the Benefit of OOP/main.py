from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def game():
  question_bank = []
  for question in question_data:
      question_text = question["question"]
      question_answer = question["correct_answer"]
      new_question = Question(question_text, question_answer)
      question_bank.append(new_question)
  
  quiz = QuizBrain(question_bank)
  
  while quiz.more_questions():
      quiz.next_question()
  
  print("You've completed the quiz\n")
  print(f"Your final score was: {quiz.score}/{quiz.question_number}.\n")
  if input("Play again? Type 'y' for yes and 'n' for no.\n").lower() == 'y':
    game()

game()