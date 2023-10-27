"""Stores functions to use across the program."""

import json
import csv
from datetime import date
from datetime import datetime


def validate_num(min: int, max: int) -> int:
    """Checks input is appropriate for purpose"""
    while True:
        try:
            data = int(input("Enter number: "))

        # If user tries to enter a letter.
        except ValueError:
            print("Input is not a number, please try again")
            continue

        # Check number is within range as specified.
        if data < min or data > max:
            print("Input is outside of range, please try again")
            continue
        else:
            return data


def make_type_list():
    """Creates the 16 types list used in menus."""
    types_dict = read_json_file("docs/types.json")
    print("\nWhich type would you like to know more about? ")

    # Assigns a number and prints the MBTI type name.
    num = 1
    for key in types_dict:
        print(f"  {num}  {key}")
        num += 1


def make_function_list():
    """Creates the 8 cognitive function list."""
    types_list = read_csv_file("docs/cog_functions.csv")
    print("\nWhich cognitive function would you like to know more about? ")

    # Assigns a number and prints the cognitive function name.
    num = 1
    for i in types_list:
        if len(i) < 3:
            print(f"  {num}  {i}")
            num += 1


def get_cog_type(val: int, cog_dict: dict):
    """Prints info about each MBTI type"""
    # Creating a list using the keys from created dictionary.
    type_list = []
    for keys in cog_dict.keys():
        type_list.append(keys)

    # Print the right info from user choice.
    print(cog_dict[type_list[val - 1]])
    print("\nType descriptions from psychologyjunkie.com")


def get_cog_function(val: int, cog_list: list):
    """Prints info about each cognitive function."""
    # Remove unneeded info from list.
    # Simplifies next step.
    for i in cog_list:
        if len(i) < 3:
            cog_list.remove(i)

    # Prints the right info from user choice.
    print(cog_list[val - 1])
    print("\nType descriptions from truity.com")


def read_json_file(filename: str) -> dict:
    """Read JSON files."""
    with open(filename) as t:
        # Create a dictionary containing json file.
        types_dict = json.load(t)
    return types_dict


def read_csv_file(filename: str) -> list:
    """# Read CSV files."""
    with open(filename) as quest_file:
        read = csv.reader(quest_file)
        q_list = []
        for row in read:
            # The question itself.
            q_list.append(row[0])
            # Which score the question relates to.
            q_list.append(row[1])
        return q_list


def get_date():
    """Gets today's date, used for output."""
    return date.today()


def get_time():
    """Gets current time, used for output."""
    return datetime.now().strftime("%H:%M:%S")
