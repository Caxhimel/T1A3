import csv

class User:
    def __init__(self):
        self.user_scores = {"Fe": 0, "Fi": 0, "Te": 0, "Ti": 0, "Ne": 0, "Ni": 0, "Se": 0, "Si": 0}
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
        while(self.iterator < len(self.q_list) - 1):
            print("Please enter a number from 1 - 5 to indicate how much you agree with each statement")
            # Print the question
            print(self.q_list[self.iterator])
            self.answer = input()
            # When user answers a question, store answer in the correct category
            self.user_scores[self.q_list[self.iterator + 1]] = self.answer
            # Add 2 because we need to skip the answer sorting info for the question
            self.iterator += 2


