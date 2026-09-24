import random

questions = [
    {
        "question": "What is 15 + 7?",
        "options": ["20", "21", "22", "23"],
        "answer": "22",
        "category": "Maths"
    },
    {
        "question": "What is 9 x 6?",
        "options": ["45", "54", "56", "63"],
        "answer": "54",
        "category": "Maths"
    },
    {
        "question": "What is 81 ÷ 9?",
        "options": ["7", "8", "9", "10"],
        "answer": "9",
        "category": "Maths"
    },
    {
        "question": "What is 100 - 37?",
        "options": ["53", "63", "73", "67"],
        "answer": "63",
        "category": "Maths"
    },
    {
        "question": "What is 12 x 8?",
        "options": ["86", "96", "106", "108"],
        "answer": "96",
        "category": "Maths"
    },

    {
        "question": "Which organ pumps blood around the human body?",
        "options": ["Brain", "Lungs", "Heart", "Kidney"],
        "answer": "Heart",
        "category": "Science"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "H2O",
        "category": "Science"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Venus", "Earth", "Mercury", "Mars"],
        "answer": "Mercury",
        "category": "Science"
    },
    {
        "question": "What force keeps us on the ground?",
        "options": ["Magnetism", "Gravity", "Friction", "Electricity"],
        "answer": "Gravity",
        "category": "Science"
    },
    {
        "question": "How many planets are in our Solar System?",
        "options": ["7", "8", "9", "10"],
        "answer": "8",
        "category": "Science"
    },

    {
        "question": "What is the capital of France?",
        "options": ["Madrid", "Rome", "Paris", "Berlin"],
        "answer": "Paris",
        "category": "General Knowledge"
    },
    {
        "question": "Which is the largest continent?",
        "options": ["Africa", "Europe", "Asia", "North America"],
        "answer": "Asia",
        "category": "General Knowledge"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yuan", "Won", "Yen", "Ringgit"],
        "answer": "Yen",
        "category": "General Knowledge"
    },
    {
        "question": "Which country is famous for the pyramids of Giza?",
        "options": ["Egypt", "Greece", "Mexico", "India"],
        "answer": "Egypt",
        "category": "General Knowledge"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "answer": "Blue Whale",
        "category": "Science"
    },

    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo"],
        "answer": "Leonardo da Vinci",
        "category": "General Knowledge"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Computer Processing Utility"
        ],
        "answer": "Central Processing Unit",
        "category": "Science"
    },
    {
        "question": "Which ocean is between Africa and Australia?",
        "options": [
            "Atlantic Ocean",
            "Pacific Ocean",
            "Indian Ocean",
            "Arctic Ocean"
        ],
        "answer": "Indian Ocean",
        "category": "General Knowledge"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6",
        "category": "Maths"
    },
    {
        "question": "Which language is primarily used to style web pages?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "CSS",
        "category": "General Knowledge"
    }
]





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




    

