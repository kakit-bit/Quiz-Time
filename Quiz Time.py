# Script imports pre-set quiz questions, options and answer from .csv file
# Script converts .csv questions into class objects and randomizes question order
# User is prompted for answer input
# Script returns number of mistakes made

import time as t
import matplotlib as plt
import random

# Class saves question data in to a Profile Object
class Question():
    def __init__(self, quiz_question, choice_a, choice_b, choice_c, choice_d, quiz_answer):
        self.quiz_question = quiz_question
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d
        self.quiz_answer = quiz_answer

# Function Opens .csv File to Save questions, choices and answer into List
def harvest_csv():
    import csv
    target_file = open("quiz.csv")
    csv_reader_object = csv.reader(target_file)

    question_list = []

    for item in csv_reader_object:
        question_list.append(item)

    return question_list

# Function converts list of questions harvested from .csv into a list of Class objects
def csv_to_class(question_list):
    class_question_list = []
    num = 0

    for item in question_list:
        quiz_question = question_list[num][0]
        choice_a = question_list[num][1]
        choice_b = question_list[num][2]
        choice_c = question_list[num][3]
        choice_d = question_list[num][4]
        quiz_answer = question_list[num][5]

        num += 1

        question = Question(quiz_question, choice_a, choice_b, choice_c, choice_d, quiz_answer)

        class_question_list.append(question)

    return class_question_list

# Function individually prompts user for their guess
def get_user_input():
    while True:
        user_input = input("Enter your guess: ")
        # Check if Input is a Valid Choice
        if not check_user_input(user_input):
            print("Not a valid input")
            continue
        return user_input

# Function checks validity of user input
def check_user_input(user_input):
    if str(user_input)=="1" or str(user_input)=="2" or str(user_input)=="3" or str(user_input)=="4":
        return True
    else:
        return False

# Function checks answer
def check_answer(user_input,class_question_list,num):
    if (user_input) == "1":
        user_target = class_question_list[num].choice_a
    elif (user_input) == "2":
        user_target = class_question_list[num].choice_b
    elif (user_input) == "3":
        user_target = class_question_list[num].choice_c
    elif (user_input) == "4":
        user_target = class_question_list[num].choice_d

    if (user_target) == (class_question_list[num].quiz_answer):
        return True
    else:
        return False

# Function cycles through questions sequentially
def prompt_user(class_question_list):
    num = 0
    mistakes = 0
    for item in class_question_list:
        question_number = num + 1
        print("Question #", question_number, class_question_list[num].quiz_question)
        print("1. ", class_question_list[num].choice_a)
        print("2. ", class_question_list[num].choice_b)
        print("3. ", class_question_list[num].choice_c)
        print("4. ", class_question_list[num].choice_d)

        user_input = get_user_input()

        if check_answer(user_input, class_question_list, num) == False:
            mistakes += 1
            print("Incorrect!")
        else:
            print("Correct!")

        print("")
        num += 1

    return mistakes

# Function measures time to answer question - NOT IN USE
def time_in_sec():
    times = []
    start_time = t.time()
    # Function to accept user input
    end_time = t.time()
    time_elapsed = end_time - start_time

    times.append(time_elapsed)

    return times

if __name__ == '__main__':

    # Intialize questions from .csv
    question_list = harvest_csv()
    class_question_list = csv_to_class(question_list)

    # Randomize order of quiz questions
    random.shuffle(class_question_list)

    # Prompt user with questions and display final score
    user_score = prompt_user(class_question_list)

    if user_score >= 1:
        print("Number of mistakes: ", user_score)
    else:
        print("Congratulations on a perfect score!")