#TODO make take test work
#TODO make learn about function work
#TODO make quit function work
#TODO catch error in input entry, user shouldn't enter text
#TODO make sure open files closed
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
    while selection < 1 or selection > 3:
        print("Please enter the number below to make selection: ")
        selection = int(input())

    # When user enters a valid choice        
    if selection == 1:
        test = classes.Quiz()
        test._set_name()
        test._ask_questions()
        test._tab_results()

    elif selection == 2:
        print("dictionary")

    # Covers selection 3
    else:
        # Just end the program
        pass
        
call_menu()