import tools

class Glossary:
    def _start_gloss(self):
        print("What would you like to know more about?")
        print("  1  Psychological Types")
        print("  2  Cognitive Functions")
        answer = tools.validate_num(1, 2)
        
        if answer == 1:
            tools.make_type_list()
            answer = tools.validate_num(1, 16)
            tools.get_cog_type(answer,tools.read_json_file("docs/types.json"))
            
        else:
            tools.make_function_list()
            answer = tools.validate_num(1, 8)
            tools.get_cog_function(answer,tools.read_csv_file("docs/cog_functions.csv"))
            pass


            

