# sys is a module. It lets us access command line arguments, which are stored in sys.argv

import sys
import random

if len(sys.argv) < 2:
    print("Please supply a flash card file.")
    exit(1)

flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")

questions_dict = {}

for line in f:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    questions_dict[question] = answer

f.close()

print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' to quit.")
print("")

questions = list(questions_dict.keys())

i = 0
while True:
    question = random.choice(questions)
    answer = questions_dict[question]
    i = i + 1
    print("Question " + str(i) + ": " + question)
    user_input = input("Your guess: ")
    if user_input == "quit":
        print("Thanks for playing! Bye.")
        break
    elif user_input == answer:
        print("Correct answer!\n")
    else:
        print("Sorry, the answer was: " + answer + "\n")
