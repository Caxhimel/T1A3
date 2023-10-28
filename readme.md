# Michael Bartel T1A3 - Console App

This project allows the user to take a personality test.  This test is based on identifying methods of thinking (these methods are referred to as cognitive functions).  The cognitive functions were identified by Swiss Psychologist Carl Jung.  Since Jung, other psychologists have further developed his theories.  In use today is a theory called the Myers-Briggs Type Indicator (MBTI).

MBTI has attempted to create 16 personality types based on these cognitive functions.  There are 8 functions, which are combined into groupings of 4 (called a stack).  However, the first two functions are what defines a type, the last two are just the opposites of the first two.

The functions are as follows: <br>

Judging functions:
* Introverted Thinking (Ti)
* Extroverted Thinking (Te)
* Introverted Feeling (Fi)
* Extroverted Feeling (Fe)

Perceiving functions:
* Introverted Sensing (Si)
* Extroverted Sensing (Se)
* Introverted Intuition (Ni)
* Extroverted Intuition (Ne)

Judging functions enable a user to make decisions.  Perceiving functions enable a user to gather information.  Each function has an introverted (subjective, inward-focussed) and an extroverted (objective, outward-focussed) version.  The combination of these functions give a user a way to:

1. Gather data about themselves
1. Gather data about the outside world
1. Make decisions about themselves
1. Make decisions about the outside world

Here are all the types:
![chart of types](docs/types%20chart.jpg)[^1]

This test aims to determine a user's type based up their strongest functions, according to the rules of the MBTI system.

* Each person gets two introverted functions, and two extroverted funtions
* These functions alternate in order.  Either E I E I  or  I E I E
* Each person gets two judging and two perceiving functions.  
* In the following order: J P P J  or  P J J P.

Type will be determined by as follows:
1. Ask questions to determine the strongest function
1. Determine if that function is judging or perceiving, and extroverted or introverted
1. Find the strongest opposite type function

For Example, if Extraverted Feeling (Fe) was the highest scoring function, then the second function must be either Introverted Sensing (Si) or Introverted Intuition (Ni).  If (Si) was the highest score between those two, then the user would be an ESFJ.  This is how we can programmatically determine a user's type.

Author's Notes:  Because this is primarily a programming assessment, the test has been greatly simplified (to facilitate marking).  As such, it does not contain enough information to make a thorough assessment of personality.

As psychology is a soft science, the quality of its results depend on the knowledge of the individual.  The answers gained should be considered as starting points for self-awareness and personal growth, rather than as absolute truth.

As this is a programming assignment, the author does not recommend using this software an an exclusive reference for personality.  If the user wants further information on this subject, the following links are provided:<br><br>

[Official Myers-Briggs Website](https://www.themyersbriggs.com/en-US/)<br>
Official source for the MBTI test.  Provides formal certification and testing.

[Michael Caloz's cognitive function test](https://www.michaelcaloz.com/personality/)<br>
A quick but detailed test for the cognitive functions that the theory is based on.  Combines insights from David Keirsey's temperment research.

[MBTI Notes](https://mbti-notes.tumblr.com/)<br>
Detailed information about the functions, including how they affect a person based on where they are in the stack

[Psychology Junkie](https://www.psychologyjunkie.com/)<br>
Light articles that explore application of the theory in daily life.  Produced by a MBTI certified professional.

## Source Code Repository
[Github](https://github.com/Caxhimel/T1A3)

## Style Guide ##
[PEP8](https://pep8.org/)[^2]

## Features

### Take personality test
Allows the user to take the basic personality test as described above
### Learn about MBTI
A small reference section to describe the personality types and cognitive functions that users may consult if interested.
### Export results
Ability to save the test results into an external file.  The allows the user to access their results without having to do the test again.

## Project management screenshots
Wrote design plan
![Alt text](<docs/Screenshot 1.png>)

Found and setup project management software
![Screenshot 2](<docs/Screenshot 2.png>)

Completed project setup tasks - github, create readme
![Screenshot 3](<docs/Screenshot 3.png>)

Create basic parts of program - menu, display questions, get answers
![Screenshot 4](<docs/Screenshot 4.png>)

Added extras section (add more questions)
![Screenshot 5](<docs/Screenshot 5.png>)

Added more to extras section (tabulation algorithm)
![Screenshot 6](<docs/Screenshot 6.png>)

Finished tabulate results
![Screenshot 7](<docs/Screenshot 7.png>)

Finished output results
![Screenshot 8](<docs/Screenshot 8.png>)

Finished glossary feature (Learn about MBTI)
![Screenshot 9](<docs/Screenshot 9.png>)

Finished making bash script<br>
Renamed task 6 to better reflect task<br>
Added to task 9 to improve bash script
![Screenshot 10](<docs/Screenshot 10.png>)

Finished documentation
![Screenshot 21](<docs/Screenshot 21.png>)

Finished presentation
![Screenshot 22](<docs/Screenshot 22.png>)


## Help Documentation
### Hardware requirements
As the Python Software Foundation does not officially list any hardware requirements, the following suggestions are sourced externally.

    Modern Operating System:
        Windows 7 or 10
        Mac OS X 10.11 or higher, 64-bit
        Linux: RHEL 6/7, 64-bit (almost all libraries also work in Ubuntu)
    x86 64-bit CPU (Intel / AMD architecture). ARM CPUs are not supported.
    4 GB RAM
    5 GB free disk space
[Source: Enthought ](https://support.enthought.com/hc/en-us/articles/204273874-Enthought-Python-Minimum-Hardware-Requirements)

### Dependencies
Python 3.10

### How to install application
Assuming user has unzipped file to access this document
1. Open terminal application 
2. Navigate to where the files were unzipped to
3. Enter the following command in the terminal
```
chmod +x run_program.sh
```
4. Enter this command in the terminal
```
./run_program.sh
```
The program should now begin

## How to use the program
![Screenshot 11](<docs/Screenshot 11.png>)

You are on the main menu, and the system is waiting for input.  Type a number and press enter.  The number you type should be the number next to the item you want to choose.

There are three options here.
1. Take MBTI test
2. Learn about MBTI
3. Quit

### Take MBTI test
![Screenshot 12](<docs/Screenshot 12.png>)

After entering the number 1 and pressing enter, you will be asked for your name.  Type in anything (or don't, it's fine) and press enter.

![Screenshot 13](<docs/Screenshot 13.png>)

You are now given a question and information about inputting answers.  You are being asked to enter a number from 1 to 5 that indicates how accurately the statement represents you.<br>
* If the statement is entirely wrong about you, type 1.
* If the statement is just a little true, type 2.
* If the statement is half true, type 3.
* If the statement is mostly true, type 4.
* If the statement is very accurate about you, type 5.

Make your choice and press enter.

Note that there are no wrong answers here. Try to answer the questions with regard to how you think most of the time, rather than under specific circumstances.

This will be repeated for every question, then you will see:
![Screenshot 14](<docs/Screenshot 14.png>)

These are your results.  It is possible to get more than one result with this test.  This is intended, it can be hard to know yourself well enough for a test to measure your true personality. These results serve as a launching point for further study and personal growth.

Finally, you are asked if you wish to have a copy of the test results.  This can be useful if you want to keep a record of your result (so you don't have to take the test again).

![Screenshot 15](<docs/Screenshot 15.png>)

If you choose y, the system will save your results into a text file.  You can find the file in the unzipped folder.  If you choose n, then none of that will happen.  Either way, you will be back at the menu.

### Learn about MBTI
Choosing option 2 presents more detail about different parts of MBTI.

![Screenshot 16](<docs/Screenshot 16.png>)

You can get information about your type (like what you might have been told by the test), and about the cognitive functions (which the test asks about).

Choosing option 1 generates a list of all 16 potential MBTI types.
![Screenshot 17](<docs/Screenshot 17.png>)
Choose an option that you would like to know more about.

![Screenshot 18](<docs/Screenshot 18.png>)
A paragraph of text explaining the type will appear (read in from an external JSON file).  The menu is again displayed.

![Screenshot 19](<docs/Screenshot 19.png>)
A list of all 8 cognitive functions are generated.  Select one in the same way as above.

![Screenshot 20](<docs/Screenshot 20.png>)
Information about the function is printed and the menu shown.

### Quit
You may enter option 3 during the starting menu to close the program.



## Sources
[^1]: Butt, J. (no date) Functional Analysis, Functional analysis of psychological types. Available at: https://typelogic.com/fa.html (Accessed: 22 October 2023). 

[^2]:Rossum , G. van, Warsaw, B. and Coghlan, A. (2013) PEP 8 – Style Guide for Python Code, Python enhancement proposals. Available at: https://peps.python.org/pep-0008/ (Accessed: 22 October 2023). 
