# Separate file to store functions to use across the program

import json
import csv
from datetime import date
from datetime import datetime

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
    types_list = read_csv_file("docs/cog_functions.csv")
    print("\nWhich cognitive function would you like to know more about? ")
    num = 1
    for iter in types_list:
        if len(iter) < 3:
            print(f"  {num}  {iter}")
            num += 1

def get_cog_type(val: int, cog_dict: dict):
        # Creating a list using the keys from created dictionary
        # Need something I can refer to by index with only needed info
        type_list = []
        for keys in cog_dict.keys():
            type_list.append(keys)

        print(cog_dict[type_list[val - 1]])
        print("\nType descriptions from psychologyjunkie.com")

def get_cog_function(val: int, cog_list: list):
        for iter in cog_list:
             if len(iter) < 3:
                cog_list.remove(iter)
        print(cog_list[val-1])
        print("\nType descriptions from truity.com")

def read_json_file(filename):
    with open(filename) as t:
        # Create a dictionary containing json file
        types_dict = json.load(t)
    return types_dict

def read_csv_file(filename):
    with open(filename) as quest_file:
        read = csv.reader(quest_file)
        q_list = []
        for row in read:
            # The question itself
            q_list.append(row[0])
            # Which score the question relates to
            q_list.append(row[1])
        return q_list

def get_date():
    return date.today()

def get_time():
    return datetime.now().strftime("%H:%M:%S")