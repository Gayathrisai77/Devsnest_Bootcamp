#KAUN BANEGA CROREPATI

name = input("Enter your name:")
print(f"welcome to KBC {name}")
print(f"Lets start the game {name}")
print("Here are some rules to follow")
score = 0
question_no = 0
print("you have 15 questions to Answer Each correct Answer you will get suffient amout")
Questions = [
"1.How many players are there in a cricket team?\n [A] 11\n [B] 10\n [C] 6\n [D] 13\n",
"2.which country is considered as the birthplace of cricket?"\n [A] India\n [B]
Engaland\n [C] Australia\n [D] SouthAfrica\n",
"3.When Virat Kohli was awarded with the Arjuna Award?\n [A] 2012\n [B] 2007\n [c]2000\n [D] 2013\n",
"4."
]



























#KAUN BANEGA CROREPATI

name = input("Enter your name:")
print(f"welcome to KBC {name}")
print(f"Lets start the game {name}")
print("Here are some rules to follow")
score = 0
question = 0
class Question:
 def __init__(self,prompt,answer):
  self.prompt = prompt
  self.answer = answer
  
  
print("you have 15 questions to Answer Each correct Answer you will get suffient amout")
question_prompts = [
"How many players are there in a cricket team?\n [A] 11\n [B] 10\n [C] 6\n [D] 13\n",
"which country is considered as the birthplace of cricket?\n [A] India\n [B]Engaland\n [C] Australia\n [D]SouthAfrica\n",
"When Virat Kohli was awarded with the Arjuna Award?\n [A] 2012\n [B] 2007\n [c]2000\n [D] 2013\n",
"In cricket,what does LBW stand for?\n [A]Leg Before Wicket\n [B]Left Batsman Wrong\n [C]Leg Ball Wasted\n [D] Lost Bat Winner\n",                              "ket ?\n [A]Mumbai\n [B]Kolkata\n [C]chennai\n [D] Delhi\n"
]
my_questions = [
  question(question_prompts[0], "A"),
  question(question_prompts[1], "c"),
  question(question_prompts[2], "D"),
  question(question_prompts[3], "A"),
  question(question_prompts[4], "B")
]
def run_test(my_questions):
  score = 0
  for question in my_questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("you got" + str(score) + "/" + 
  str(len(questions)) + "correct")
run_test(my_questions)
print(4*"\n")











































