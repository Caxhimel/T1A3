import tools

class Glossary:
    # def __init__(self):
        # self.types_list = {"ESFJ": "", "ISFJ": "", "ESTJ": "", "ISTJ": "", 
        #                    "ENFJ": "", "INFJ": "", "ENFP": "", "INFP": "",
        #                    "ESFP": "", "ISFP": "", "ESTP": "", "ISTP": "",
        #                    "ENTJ": "", "INTJ": "", "ENTP": "", "INTP": "" }

    def _start_gloss(self):
        print("What would you like to know more about?")
        print("  1  Psychological Types")
        print("  2  Cognitive Functions")
        answer = tools.validate_num(1, 2)
        
        if answer == 1:
            tools.make_type_list()
            answer = tools.validate_num(1, 16)
            tools.get_type(answer,tools.read_json_file("docs/types.json"))
            
        else:
            print("Which cognitive function would you like to know more about? ")
            tools.make_function_list()
            pass


            

