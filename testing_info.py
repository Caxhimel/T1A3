"""Outline of testing procedure"""

# This document contains information about two tests.  These tests 
# determine if the program is producing the expected output.

# Test 1:
# Check that validate_num() generates the expected output.

# Purpose:
# validate_num() is a function that takes input from the user, then
# checks for errors, and returns a result that can be used in later
# functions.

# Expected input:
# Text entered by the user.  Text is gathered from input().
# Text will be received as a string.

# Expected output:
# Integer, between min and max values (passed into function).

# Checks done:
# Function first tries to convert string to integer.  If unable, 
# generates error.  User is asksed again for input and informed
# why input was invalid.

# If type cast succeeds, checks that integer is within the
# accepted range (as passed into function).  If so, integer is
# returned as output of function.  If not, user is informed and
# asked to enter input again.

# Testing methodology:
# 1. Run program until user is asked for input that calls
#    validate_num().  First call is at main menu.
# 2. Try entering the following inputs (expected result below):
#    - number within the accepted range (eg. 1, 2, 3)
#        - PASS
#    - number outside the accepted range (eg. 32, -1)
#        - FAIL
#    - a symbol (eg. +, =, &)
#        - FAIL
#    - letters (a, the)
#        - FAIL
#    - a string with a number ("1")
#        - FAIL
#    - nothing (just press enter)
#        - FAIL

# Test 2:
# Check that tab_results() generates the expected output.

# Purpose:
# This test checks that tab_results() correctly implements
# the requirements of the Myers-Briggs type indicator, to the
# results of a questionnaire provided to the user.

# Expected Input:
# The function itself takes no input.  But it uses information
# from the containing class.  The function modifies attributes
# within the class. It expects information about the user's category
# scores to be entered and variables and lists to store data.

# Expected Output:
# The function itself returns no output. But it changes information
# within the containing class.  The end result is that the user_type
# variable (string), will be updated with text that lists the user's
# potential psychological type (according to MBTI rules).

# Checks done:
# The function ultimately iterates over a list that contains the
# highest scores from the questionnaire.  For each score, the function
# consults a match/case structure to check for the second highest score
# that is relevant to the MBTI rules.  If the data does not match any
# known type, the function will give a message that the user's type cannot
# be determined by MBTI rules.  This should not happen but it is there if
# needed.

# Testing Methodology:
# At the start of each question, I have included the relevant cognitive
# function that the answer will score against.  To get a specific result,
# a user must give high scores to the correct questions.

# +------+-----+-----+    +------+-----+-----+
# | Type | Dom | Aux |    | Type | Dom | Aux |
# +------+-----+-----+    +------+-----+-----+
# | ESFJ | Fe  | Si  |    | ESFP | Se  | Fi  |
# | ISFJ | Si  | Fe  |    | ISFP | Fi  | Se  |
# | ESTJ | Te  | Si  |    | ESTP | Se  | Ti  |
# | ISTJ | Si  | Te  |    | ISTP | Ti  | Se  |
# | ENFJ | Fe  | Ni  |    | ENTJ | Te  | Ni  |
# | INFJ | Ni  | Fe  |    | INTJ | Ni  | Te  |
# | ENFP | Ne  | Fi  |    | ENTP | Ne  | Ti  |
# | INFP | Fi  | Ne  |    | INTP | Ti  | Ne  |
# +------+-----+-----+    +------+-----+-----+

# To use this table, first find the type you want to
# test for.  The Dom column tells you which question should be
# answered with a highest score (5).  The Aux column tells
# you which question should be answered with the second highest 
# score.(4)

# Note: It is possible (and intended) to get multiple types for
# a user's results (depending on their answers).  The below procedure
# will generate a single result.  You may generate multiple type
# results by giving the highest score to more than one question.

# FE I am driven by a desire to help others. I think about others needs more than my own.
# input: 5
# SI I am driven by a desire for stability.  I stick to what I know.
# input: 4
# Type: ESFJ