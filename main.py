#TODO make take test work
#TODO make learn about function work
#TODO make quit function work
#TODO catch error in input entry, user shouldn't enter text
#TODO make sure open files closed
#check style guide again

import classes

def call_menu():
    print("\nMain Menu\n")
    print("  1   Take MBTI test")
    print("  2   Learn about MBTI")
    print("  3   Quit")

    selection = 0

    while selection < 1 or selection > 3:
        print("Please enter the number below to make selection: ")
        selection = int(input())
            
    if selection == 1:

        test = classes.User()
        test.set_name()

    elif selection == 2:
        print("dictionary")

    else:
        quit()
        
call_menu()
# test = classes.User("Pete")
# print(test.q_list[0])
# print(test.q_list[1])