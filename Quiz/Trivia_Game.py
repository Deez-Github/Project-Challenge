import random
import json
import os


def load_questions():
    try:
        file_path = os.path.join(
            os.path.dirname(__file__),
            "questions.json"
        )

        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("ERROR: questions.json was not found.")
        return []

    except json.JSONDecodeError as error:
        print("ERROR: Invalid JSON.")
        print(error)
        return []


questions = load_questions()

print("Loaded questions:", len(questions))
def quiz(questions):
    print("==========================")
    print("Terminal QUIZ")
    print("==========================")
    print()
    score = 0
    random.shuffle(questions)
    letters = ["A", "B", "C", "D"]
    for question in questions:
        print(question["question"])
        #randomize options
        random.shuffle(question["options"])
        for index, option in enumerate(question["options"]):
            print(f"{letters[index]}. {option}")
        while True:
            ans = input("What is your answer: ").strip().upper()
            if ans in letters:
                selected_answer = question["options"][letters.index(ans)]
                break
            elif ans in question["options"]:
                selected_answer = ans
                break
            else:
                print("Please choose one of the available answers.")


        if selected_answer == question["answer"]:
            score += 1
            print("correct!")
        else:
            print("Wrong")
            print(f"Correct Answer: {question['answer']} ")

    print("==========================")
    print("QUIZ FINISHED")
    print("==========================")
    print()

    print (f"Your score: {score}/{len(questions)}")
    print (f"Percentage: {round((score/len(questions)) * 100,2)}%")


def maths_quiz():
  maths_questions = []

  for question in questions:
    if question["category"] == "Maths":
      maths_questions.append(question)
  quiz(maths_questions)
  
          
def science_quiz():
  science_question = []

  for question in questions:
    if question["category"] == "Science":
      science_question.append(question)

  quiz(science_question)


def generalKnowledge_Quiz():
  generalKnowledge_question = []
   
  for question in questions:
    if question["category"] == "General Knowledge":
      generalKnowledge_question.append(question)
   
  quiz(generalKnowledge_question)

def all_quize():
   quiz(questions)

 

def show_menu():
    print("===== QUIZ =====\n")
    print("1. Maths")
    print("2. Science")
    print("3. General Knowledge")
    print("4. All")
    print("5. Exit")


while True:

    show_menu()
    
    choice = input("Enter your Choice: ").strip()


    if choice == "1":
      print("Welcome to Maths Quiz")
      maths_quiz()
        
    elif choice == "2":
      print("Welcome to Science Quiz")
      science_quiz()

    elif choice == "3":
      print("Welcome to General Knowledge Quiz")
      generalKnowledge_Quiz()
    elif choice == "4":
      print("Welcome to All Assessment")
      all_quize()
    elif choice == "5":
      print("Goodbye")
      break
    
    else:
      print("Invalid Choice")


