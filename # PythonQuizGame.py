# Python Quiz Game

questions = ("How many elements are there in the periodic table of elements?:",
             " Which animal lays the largest eggs?:",
             "What is the most abundant gas in Earths Atmosphere?:",
             "How many bones are in the human body?:",
             "Which planet in the solar system is the largest?:")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Jupiter", "D. Mars"))
            

answers = ('C','D','A','A','B')

score = 0

question_num = 0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ")


    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")

    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------------")
print(        "Results"       )
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer , end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")