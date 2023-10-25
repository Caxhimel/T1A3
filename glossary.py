"""Handles running the glossary function"""

import tools


class Glossary:
    """Stores information to operate glossary function"""
    # Creates glossary menu.
    def _start_gloss(self):
        print("What would you like to know more about?")
        print("  1  Psychological Types")
        print("  2  Cognitive Functions")
        # Get user's selection.
        answer = tools.validate_num(1, 2)

        if answer == 1:
            # Produce list of 16 MBTI types.
            tools.make_type_list()
            # Get their selection.
            answer = tools.validate_num(1, 16)
            # Print the details about the chosen type.
            tools.get_cog_type(answer, tools.read_json_file("docs/types.json"))

        else:
            # Produce the list of 8 cognitive functions.
            tools.make_function_list()
            # Get their selection.
            answer = tools.validate_num(1, 8)
            # Print the details about the chosen cognitive function.
            tools.get_cog_function(
                answer, tools.read_csv_file("docs/cog_functions.csv"))
