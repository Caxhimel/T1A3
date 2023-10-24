#TODO make take test work
#TODO make learn about function work
#TODO make quit function work
#TODO catch error in input entry, user shouldn't enter text
#TODO make sure open files closed
#TODO make tab_results handle multiple top functions
#TODO cleanup question files
#TODO check if file opens successfully
#check style guide again

import quiz
import glossary
import tools

# Main menu
def call_menu():
    print("\nMain Menu, Please type the number that matches your selection and press return\n")
    print("  1   Take MBTI test")
    print("  2   Learn about MBTI")
    print("  3   Quit")

    selection = tools.validate_num(1,3)

    # When user has entered a valid choice
    # Run the test
    if selection == 1:
        test = quiz.Quiz()
        test._set_name()
        test._ask_questions()
        test._tab_results()
        print(test.user_type)
        test._output_results()

    # Learn about MBTI
    elif selection == 2:
        learn = glossary.Glossary()
        learn._start_gloss()

    # Covers selection 3
    elif selection == 3:
        # Just end the program
        pass
    else:
        pass
        
        
call_menu()