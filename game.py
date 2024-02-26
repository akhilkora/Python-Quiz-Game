# Goal: Quiz Game in Python
# Requirements:
#   - Create a series of Questions with options
#   - Keep Answer Keys
#   - Ask users all the questions one by one
#   - Prompt for an answer with choices explicitly shown
#   - Everytime there is a correct answer, increase score by 1, Show user if it is correct or not.
#   - In the end, present the score as final result

# Create a series of questions with options
questions = ("What is the fastest land animal?:",
             "Who is the richest person alive?:",
             "Who is the fastest person alive?:",
             "What is the largest animal alive?:",
             )

options = (("A. Bison","B. Cheetah", "C. deer"), 
           ("A. Elon Musk", "B. Jeff Bezos", "C. Mr.Beast"),
           ("A. Ronaldo", "B. Yohan Blake", "C. Usain Bolt"),
           ("A. Blue Whale", "B. Elephant", "C. Giraffe")
           )
# Create Answer Keys
answers = ("B", "A","C","A")

# Initialize question_num to 0
qno = 0

# Initialize score to 0
score = 0

# Loop through all questions
for question in questions:
    # Display question & options
    print(question)
    for option in options[qno]:
        print(option)
    # Prompt user for an answer
    guess = input("Enter your answer A, B, or C")
    if(guess.lower() == answers[qno].lower()):
        print("\033[1;32mCorrect\033[0m")
        # Answer is correct, increment the score
        score=score+1
    else:
        # Answer is incorrect, provide the feedback to the user.
        print("\033[1;31mincorrect\033[0m, Correct answer is: " + answers[qno])
    # Increment the question number    
    qno = qno+1

# Calculate the percentage
percentage = int((score / len(questions)) * 100)

# Print the final Score
print(f"Your score is: {percentage}%")
