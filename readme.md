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
### Type information
A small reference section to describe the personality types and cognitive functions that users may consult if interested.
### Export results
Ability to save the test results into an external file.  The allows the user to access their results without having to do the test again.

## Project management screenshots
wrote design plan
![screenshot](docs/screenshot%201.png)

found and setup project management software
![screenshot](docs/screenshot%202.png)

completed project setup tasks - github, create readme
![screenshot](docs/screenshot%203.png)

create basic parts of program - menu, display questions, get answers
![screenshot](docs/screenshot%204.png)

added extras section (add more questions)
![screenshot](docs/screenshot%205.png)

added more to extras section (tabulation algorithm)
![screenshot](docs/screenshot%206.png)

finished tabulate results
![screenshot](docs/screenshot%207.png)

finished output results
![screenshot](docs/screenshot%208.png)


## Sources
[^1]: Butt, J. (no date) Functional Analysis, Functional analysis of psychological types. Available at: https://typelogic.com/fa.html (Accessed: 22 October 2023). 

[^2]:Rossum , G. van, Warsaw, B. and Coghlan, A. (2013) PEP 8 – Style Guide for Python Code, Python enhancement proposals. Available at: https://peps.python.org/pep-0008/ (Accessed: 22 October 2023). 
