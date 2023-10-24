#TODO make take test work
#TODO make learn about function work
#TODO make quit function work
#TODO catch error in input entry, user shouldn't enter text
#TODO make sure open files closed
#TODO make tab_results handle multiple top functions
#TODO cleanup question files
#TODO check if file opens successfully
#check style guide again

import classes

# Main menu
def call_menu():
    print("\nMain Menu\n")
    print("  1   Take MBTI test")
    print("  2   Learn about MBTI")
    print("  3   Quit")

    selection = 0

    # Error handling, user can only enter number 1-3, retry if invalid
    while True:
        try: 
            selection = int(input())
            break
        except ValueError:
            print("Please enter a number from 1 - 5")

    # When user has entered a valid choice
    # Run the test
    if selection == 1:
        test = classes.Quiz()
        test._set_name()
        test._ask_questions()
        test._tab_results()
        print(test.user_type)
        test._output_results()
        
    # Learn about MBTI
    elif selection == 2:
        print("dictionary")

    # Covers selection 3
    else:
        # Just end the program
        pass
        
call_menu()