# Separate file to store functions to use across the program

import json
import csv

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
            
def make_type_list():
    types_dict = read_json_file("docs/types.json")
    print("\nWhich type would you like to know more about? ")
    num = 1
    for key in types_dict:
        print(f"  {num}  {key}")
        num += 1

def make_function_list():
    types_dict = read_json_file("docs/types.json")
    print("\nWhich cognitive function would you like to know more about? ")
    num = 1
    for key in types_dict:
        print(f"  {num}  {key}")
        num += 1

def get_type(val: int, dictionary: dict):
        # Creating a list using the keys from created dictionary
        # Need something I can refer to by index
        type_list = []
        for keys in dictionary.keys():
            type_list.append(keys)
        print(dictionary[type_list[val -1]])
        print("\nType descriptions from psychologyjunkie.com")

def read_json_file(filename):
    with open(filename) as t:
        # Create a dictionary containing json file
        types_dict = json.load(t)
    return types_dict

def read_csv_file(filename):
    with open("docs/questions.csv") as quest_file:
        read = csv.reader(quest_file)
        q_list = []
        for row in read:
            # The question itself
            q_list.append(row[0])
            # Which score the question relates to
            q_list.append(row[1])
        return q_list
