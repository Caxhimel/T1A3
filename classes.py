import csv

class Quiz:
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
        self.dom_function = max(self.user_scores, key = self.user_scores.get)
        match self.dom_function:
            case "Fe":
                if self.user_scores["Ni"] > self.user_scores["Si"]:
                    return "ENFJ"
                elif self.user_scores["Si"] > self.user_scores["Ni"]:
                    return "ESFJ"
                else:
                    return "You could be an ENFJ or ESFJ"
                
            case "Fi":
                if self.user_scores["Ne"] > self.user_scores["Se"]:
                    return "INFP"
                elif self.user_scores["Se"] > self.user_scores["Ne"]:
                    return "ISFP"
                else:
                    return "You could be an INFP or ISFP"
                
            case "Te":
                if self.user_scores["Ni"] > self.user_scores["Si"]:
                    return "ENTJ"
                elif self.user_scores["Si"] > self.user_scores["Ni"]:
                    return "ESTJ"
                else:
                    return "You could be an ENTJ or ESTJ"
                
            case "Ti":
                if self.user_scores["Ne"] > self.user_scores["Se"]:
                    return "INTP"
                elif self.user_scores["Se"] > self.user_scores["Ne"]:
                    return "ISTP"
                else:
                    return "You could be an INTP or ISTP"
                
            case "Ne":
                if self.user_scores["Ti"] > self.user_scores["Fi"]:
                    return "ENTP"
                elif self.user_scores["Fi"] > self.user_scores["Ti"]:
                    return "ESFP"
                else:
                    return "You could be an ENTP or ESFP"
                
            case "Ni":
                if self.user_scores["Te"] > self.user_scores["Fe"]:
                    return "INTJ"
                elif self.user_scores["Fe"] > self.user_scores["Te"]:
                    return "INFJ"
                else:
                    return "You could be an INTJ or INFJ"
                
            case "Se":
                if self.user_scores["Ti"] > self.user_scores["Fi"]:
                    return "ESTP"
                elif self.user_scores["Fi"] > self.user_scores["Ti"]:
                    return "ESFP"
                else:
                    return "You could be an ESTP or ESFP"
                
            case "Si":
                if self.user_scores["Te"] > self.user_scores["Fe"]:
                    return "ISTJ"
                elif self.user_scores["Fe"] > self.user_scores["Te"]:
                    return "ISFJ"
                else:
                    return "You could be an ISTJ or ISFJ"
        


