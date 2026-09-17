import random

questions =[
  {
    "question": "What is 5 + 3?",
    "options": ["6", "7", "8", "9"],
    "answer": "8"
  },
  {
    "question": "What is 10 - 4?",
    "options": ["5", "6", "7", "8"],
    "answer": "6"
  },
  {
    "question": "What is 3 x 4?",
    "options": ["7", "10", "12", "14"],
    "answer": "12"
  },
  {
    "question": "What is 20 ÷ 5?",
    "options": ["2", "3", "4", "5"],
    "answer": "4"
  },
  {
    "question": "What is 7 + 6?",
    "options": ["11", "12", "13", "14"],
    "answer": "13"
  }
]

def quiz():

    print("==========================")
    print("Terminal QUIZ")
    print("==========================")
    print()

    score = 0
    random.shuffle(questions)
    letters = ["A", "B", "C", "D"]
    for question in questions:
        print(question["question"])
        for index, option in enumerate(question["options"]):
            #random.shuffle(question["options"])
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

    print("==========================")
    print("QUIZ FINISHED")
    print("==========================")
    print()

    print (f"Your score: {score}/{len(questions)}")

quiz()

