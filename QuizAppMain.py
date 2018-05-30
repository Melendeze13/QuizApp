# Program will read in a file that is used to quiz someone
# The file will contain Questions and answers with only one that is correct
# Parse file in
# Create interface that will conduct quiz
# Run analytics i.e. quiz score
import os
import sys

filename = "Resource/Quiz#1"

# User input definition


def input_number(message):
    while True:
        try:
            userInput = int(raw_input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput

# Quiz Question implementation to create objects


class QuizQuestion:
    def __init__(self, question):
        self.question = question
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)

    def print_question(self):
        print "\n" + self.question
        for x in range(0, len(self.answers)):
            print self.answers[x].replace('\n', '').replace(' *A*', '')

    def right_answer(self, user_answer):
        correct_answer = -1
        for x in range(0, len(self.answers)):
            if " *A*" in self.answers[x]:
                correct_answer = x
        if (user_answer - 1) == correct_answer:
            return True
        else:
            return False


def main():
    print "Starting Quiz app\n"

    # Open file and check that it's valid
    with open(filename) as file_object:
        lines = file_object.readlines()

    if os.stat(filename).st_size == 0:
        print "File is empty! \nEnding Program!"
        sys.exit()

    # Make sure that the file has Name and Instructions formatted correctly
    if 'Name:' in lines[0]:
        print lines[0].replace('Name: ', '')
    else:
        print "No name found in " + filename
        sys.exit()

    if 'Instructions:' in lines[1]:
        print lines[1].replace('Instructions: ', '')
    else:
        print "No instructions found in " + filename
        sys.exit()

    # Initialize question array and loader variables
    question_array = []
    question_array_index = 0
    num_lines = sum(1 for line in lines)

    # There will always be Q1 so start with it
    question_index = 1
    question_string = "Q" + str(question_index) + ": "

    # Start loading questions and answers in question_array
    for x in range(0, num_lines - 1):

        # There will always be A1 so start with it
        # The loop will reset it to A1
        answer_index = 1
        answer_string = "A" + str(answer_index) + ": "

        # Check if line has the specific Question number
        if question_string in lines[x]:

            # Load question into question array using QuizQuestion object
            question_array.append(QuizQuestion(lines[x]))
            # Moves index forward but don't go out of bound
            if x < num_lines - 1:
                x += 1
            # Check if line has the specific Answer number
            if answer_string in lines[x]:
                while answer_string in lines[x]:
                    # Start loading answers in QuizQuestion Object
                    question_array[question_array_index].add_answer(lines[x])

                    # Increase index to and change answer string
                    # This will look for the next answer
                    answer_index += 1
                    answer_string = "A" + str(answer_index) + ": "

                    # Moves index forward but don't go out of bound
                    if x < num_lines - 1:
                        x += 1

            # Increase index to and change question string
            # This will look for the next question
            question_index += 1
            question_string = "Q" + str(question_index) + ": "
            question_array_index += 1

    quiz_score = 0

    # Start Quiz by telling the user the questions and asking for answers
    for x in range(0, len(question_array)):
        question_array[x].print_question()
        user_input = input_number("Enter a numerical number!\n")

        # If answer matches the objects correct answer add 1 to the score
        if question_array[x].right_answer(user_input):
            quiz_score += 1

    # Using the total number questions give a score out of 100
    number_questions = len(question_array)
    print "Your score is: " + str(int((float(quiz_score)/float(number_questions)) * 100)) + "/100"


if __name__ == '__main__':
    main()