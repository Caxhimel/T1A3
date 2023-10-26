"""Handles running the quiz function"""
import tools

class Quiz:
    """Stores information to handle the quiz function"""
    def __init__(self):
        # Store user's scores across the 8 cognitive functions.
        self.user_scores = {"Fe": 0, "Fi": 0, "Te": 0, "Ti": 0, "Ne": 0, "Ni": 0, "Se": 0, "Si": 0}
        # Store questions to be read in from external file.
        self.q_list = []
        # For moving through question list.
        self.iterator = 0
        # Store the user's strongest scores.
        # List is used because user may have multiple top scores.
        self.dom_func_list = []
        # String to store results of user's score calculations.
        # This string will be added to.
        self.user_type = "Your type could be:\n"
        # Date and time test taken. Used in output.
        self.current_date = tools.get_date()
        self.current_time = tools.get_time()

        # Read in questions from external file.
        self.q_list = tools.read_csv_file("docs/questions.csv")

    # Asks user for their name, used in output.
    def _set_name(self):
        self.user_name = input("Please enter your name: ")

    # Creates a text file to store user's results.
    def _output_results(self):
        answer = input("Would you like a copy of the results, y or n: ")
        while answer != "y" and answer != "n":
                print("answer invalid")
                answer = input("Would you like a copy of the results, y or n: ")
        if answer == "y":
            with open("test_results.txt", "w") as res_file:
                # Write date to result file.
                res_file.write(f"Date: {self.current_date}\n")
                # Write time test taken to result file.
                res_file.write(f"Test taken at: {self.current_time}\n")
                # Write user's name to result file.
                res_file.write(f"Name: {self.user_name}\n")
                # Write list of user's potential types to result file.
                res_file.write(f"{self.user_type}")
                
                # Write user's scores to result file.
                res_file.write(f"Your cognitive function scores are: \n")
                for key, value in self.user_scores.items():
                    res_file.write(f"{key} {value} \n")
            # Tell user the name of the file.        
            print("Results in file: test_results.txt")

    def _ask_questions(self):
        # Ask questions.
        print("\nPlease enter a number from 1 - 5 "
              "to indicate how much each statement represents you.")
        print("1 = Doesn't sound like me at all")
        print("5 = This is very much me")

        while(self.iterator < len(self.q_list) - 1):
            # Print the question.
            print(self.q_list[self.iterator])
            self.answer = tools.validate_num(1, 5)
            # When user answers a question, store answer in the correct category.
            self.user_scores[self.q_list[self.iterator + 1]] = self.answer
            # Add 2 because we need to skip the answer sorting info in the list.
            self.iterator += 2

    # Tabulate results.
    def _tab_results(self):
        # Find the highest score, may be multiple keys.
        max_score = max(self.user_scores.values())
        # Store these scores in a list, so we can process them all.
        for key, value in self.user_scores.items():
            if value == max_score:
                self.dom_func_list.append(key)

        # Go through list created above.
        for value in self.dom_func_list:
            self.dom_function = value

            # Switch statement determines which MBTI type is possible.
            # Then stores result in user_type.
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

                # If above fails, user type doesn't follow rules of MBTI
                case default:
                    self.user_type =  "MBTI cannot determine your type"
        


