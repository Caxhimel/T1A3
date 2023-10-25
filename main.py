"""Starting point for program"""

import quiz
import glossary
import tools

def call_menu():
    """Creates the main menu"""
    is_running = True
    while is_running:
        print("\nMain Menu, Please type the number that matches your selection and press return")
        print("  1   Take MBTI test")
        print("  2   Learn about MBTI")
        print("  3   Quit")

        # Get the user's selection.
        selection = tools.validate_num(1, 3)

        # Run the test.
        if selection == 1:
            test = quiz.Quiz()
            test._set_name()
            test._ask_questions()
            test._tab_results()
            print(test.user_type)
            test._output_results()

        # Learn about MBTI.
        elif selection == 2:
            learn = glossary.Glossary()
            learn._start_gloss()

        # Close the program
        else:
            is_running = False

# Create the main menu, starts the program.
call_menu()
