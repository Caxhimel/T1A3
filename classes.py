import csv

class User:
    def __init__(self):
        self.user_scores = {"fe": 0, "fi": 0, "te": 0, "ti": 0, "ne": 0, "ni": 0, "se": 0, "si": 0}
        self.q_list = []
        self.iterator = 0

        # Read in questions from external file
        with open("docs/questions.csv") as quest_file:
            read = csv.reader(quest_file)
            for self.row in read:
                # The question itself
                self.q_list.append(self.row[0])
                # Which score the question relates to
                self.q_list.append(self.row[1])

    def _set_name(self):
        self.user_name = input("Please enter your name: ")

    def _run_quiz(self):
        print("Please enter a number from 1 - 5 to indicate how much you agree with each statement")
        # Print the question
        print(self.q_list[self.iterator])
        self.answer = input()
        # When user answers a question, store answer in the correct category
        self.user_scores[self.q_list[self.iterator + 1]] = self.answer

        

