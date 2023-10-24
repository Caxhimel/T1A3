# Separate file to store functions to use across the program

import json

# Validate numerical input
def validate_num(min: int, max: int):
        while True:
            try: 
                data = int(input(f"Enter number: "))
            except ValueError:
                print("Data is not a number, please try again")
                continue
            if data < min or data > max:
                print("Data invalid, please try again")
                continue
            else:
                return data
            
def make_type_list(list: dict):

     print("\nWhich type would you like to know more about? ")
     num = 1
     for key in list:
        print(f"  {num}  {key}")
        num += 1

def get_type(val: int):
     with open('docs/types.json') as t:
        # Create a dictionary containing json file
        types_dict = json.load(t)

        # Creating a list using the keys from created dictionary
        # Need something I can refer to by index
        type_list = []
        for keys in types_dict.keys():
            type_list.append(keys)
        print(types_dict[type_list[val -1]])

     
        