import csv
import tools

class Quiz:
    def __init__(self):
        self.user_scores = {"Fe": 0, "Fi": 0, "Te": 0, "Ti": 0, "Ne": 0, "Ni": 0, "Se": 0, "Si": 0}
        self.q_list = []
        self.iterator = 0
        self.dom_function = ""
        self.dom_func_list = []
        self.user_type = "Your type could be:\n"

        # Read in questions from external file
        self.q_list = tools.read_csv_file("docs/questions.csv")

    def _set_name(self):
        self.user_name = input("Please enter your name: ")

    def _output_results(self):
        answer = ""
        answer = input("Would you like a copy of the results, y or n: ")
        while answer != "y" and answer != "n":
                print("answer invalid")
                answer = input("Would you like a copy of the results, y or n: ")
        if answer == "y":
            with open("test_results.txt", "w") as result_file:
                result_file.write(f"Name: {self.user_name}\n")
                result_file.write(f"{self.user_type}")
                result_file.write(f"Your cognitive function scores are: \n")
                result_file.write(f"Fe: {self.user_scores["Fe"]} \n")
                result_file.write(f"Fi: {self.user_scores["Fi"]} \n")
                result_file.write(f"Te: {self.user_scores["Te"]} \n")
                result_file.write(f"Ti: {self.user_scores["Ti"]} \n")
                result_file.write(f"Ne: {self.user_scores["Ne"]} \n")
                result_file.write(f"Ni: {self.user_scores["Ni"]} \n")
                result_file.write(f"Se: {self.user_scores["Se"]} \n")
                result_file.write(f"Si: {self.user_scores["Si"]} \n")
            print("Results in file: test_results.txt")
        else:
            pass

    def _ask_questions(self):
        # Ask questions
        print("\nPlease enter a number from 1 - 5 to indicate how much you agree with each statement")

        while(self.iterator < len(self.q_list) - 1):
            # Print the question
            print(self.q_list[self.iterator])
            self.answer = tools.validate_num(1, 5)
            # When user answers a question, store answer in the correct category
            self.user_scores[self.q_list[self.iterator + 1]] = self.answer
            # Add 2 because we need to skip the answer sorting info for the question
            self.iterator += 2
            # Just formatting
            print("")
            # else:
            #     print("\nInvalid answer")

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
                        self.user_type +=  "ISFP \n"
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
                    self.user_type =  "MBTI cannot determine your type"
        


