import csv

class Quiz:
    def __init__(self):
        self.user_scores = {"Fe": 0, "Fi": 0, "Te": 0, "Ti": 0, "Ne": 0, "Ni": 0, "Se": 0, "Si": 0}
        self.q_list = []
        self.iterator = 0
        self.dom_function = ""
        self.dom_func_list = []
        self.user_type = "Your type could be:\n"

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

    def _ask_questions(self):
        # Ask questions
        while(self.iterator < len(self.q_list) - 1):
            print("Please enter a number from 1 - 5 to indicate how much you agree with each statement")
            # Print the question
            print(self.q_list[self.iterator])
            self.answer = input()
            # When user answers a question, store answer in the correct category
            self.user_scores[self.q_list[self.iterator + 1]] = self.answer
            # Add 2 because we need to skip the answer sorting info for the question
            self.iterator += 2

    # Tabulate results
    def _tab_results(self):
        max_score = max(self.user_scores.values())
        for key, value in self.user_scores.items():
            if value == max_score:
                self.dom_func_list.append(key)

        for value in self.dom_func_list:
            self.dom_function = value
            # Would like to find a "DRY"er solution for this.
            match self.dom_function:
                case "Fe":
                    if self.user_scores["Ni"] > self.user_scores["Si"]:
                        self.user_type += "ENFJ\n"
                    elif self.user_scores["Si"] > self.user_scores["Ni"]:
                        self.user_type +=  "ESFJ\n"
                    else:
                        self.user_type +=  "ENFJ or ESFJ\n"
                
                case "Fi":
                    if self.user_scores["Ne"] > self.user_scores["Se"]:
                        self.user_type +=  "INFP\n"
                    elif self.user_scores["Se"] > self.user_scores["Ne"]:
                        self.user_type +=  "ISF\nP"
                    else:
                        self.user_type += "INFP or ISFP\n"
                
                case "Te":
                    if self.user_scores["Ni"] > self.user_scores["Si"]:
                        self.user_type +=  "ENTJ\n"
                    elif self.user_scores["Si"] > self.user_scores["Ni"]:
                        self.user_type +=  "ESTJ\n"
                    else:
                        self.user_type += "ENTJ or ESTJ\n"
                
                case "Ti":
                    if self.user_scores["Ne"] > self.user_scores["Se"]:
                        self.user_type +=  "INTP\n"
                    elif self.user_scores["Se"] > self.user_scores["Ne"]:
                        self.user_type += "ISTP\n"
                    else:
                        self.user_type += "INTP or ISTP\n"
                
                case "Ne":
                    if self.user_scores["Ti"] > self.user_scores["Fi"]:
                        self.user_type +=  "ENTP\n"
                    elif self.user_scores["Fi"] > self.user_scores["Ti"]:
                        self.user_type += "ESFP\n"
                    else:
                        self.user_type +=  "ENTP or ESFP\n"
                
                case "Ni":
                    if self.user_scores["Te"] > self.user_scores["Fe"]:
                        self.user_type +=  "INTJ\n"
                    elif self.user_scores["Fe"] > self.user_scores["Te"]:
                        self.user_type += "INFJ\n"
                    else:
                        self.user_type += "INTJ or INFJ\n"
                
                case "Se":
                    if self.user_scores["Ti"] > self.user_scores["Fi"]:
                        self.user_type += "ESTP\n"
                    elif self.user_scores["Fi"] > self.user_scores["Ti"]:
                        self.user_type += "ESFP\n"
                    else:
                        self.user_type += "ESTP or ESFP\n"
                
                case "Si":
                    if self.user_scores["Te"] > self.user_scores["Fe"]:
                        self.user_type += "ISTJ\n"
                    elif self.user_scores["Fe"] > self.user_scores["Te"]:
                        self.user_type += "ISFJ\n"
                    else:
                        self.user_type += "ISTJ or ISFJ\n"
                
                case default:
                    self.user_type =  "MBTI cannot work out your type"
        


