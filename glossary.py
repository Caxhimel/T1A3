import tools

class Glossary:
    def __init__(self):
        self.types_list = {"ESFJ": "", "ISFJ": "", "ESTJ": "", "ISTJ": "", 
                           "ENFJ": "", "INFJ": "", "ENFP": "", "INFP": "",
                           "ESFP": "", "ISFP": "", "ESTP": "", "ISTP": "",
                           "ENTJ": "", "INTJ": "", "ENTP": "", "INTP": "" }
    message = "Type descriptions taken from psychologyjunkie.com"

    def _start_gloss(self):
        print("What would you like to know more about?")
        print("  1  Psychological Types")
        print("  2  Cognitive Functions")
        answer = tools.validate_num(1, 2)

        if answer == 1:
            print("Which type would you like to know more about?")
            print("  1  Extrovert types")
            print("  2  Introvert types")

            answer = tools.validate_num(1, 2)
            # Make list of extroverted types
            if answer == 1:
                tools.make_type_list(self.types_list, "I")
                answer = tools.validate_num(1, 8)

            else:
                tools.make_type_list(self.types_list, "E")


        else:
            pass
            

