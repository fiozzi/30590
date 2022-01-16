# Bonus pay

At the end of the year a company rewards its employees with a bonus pay
The bonus pay is related to an "activity" score, a number in the range 0-100 that summarizes what the employee has done during the past year. 

The bonuses are defined in the file slots.txt, whose format is the following

    Type:Range:Bonus
    B0,0-29,1000
    C1,30-69,2000
    C2,70-89,3000
    ...

Type is a string of unspecified length which is unique in this file. 
For example, every employee whose score is in the range 30-69 will get a bonus of type C1 corresponding to 2000.

The number of distinc types is not specified. However, the ranges will cover the entire range 0-100. 

Scores and bonuses are integer numbers greater than 0.

You have also two other files, names.txt and scores.txt:
1) names.txt is a text file with a list of employees, each identified through a a unique identifier, with some additional data, for example:

        Name, UniqueID
        John Doe, 0234
        Jane Smith, 0022
        ...

2) scores.txt is a text file where each line has a unique identifier, matching that of an employee, and a score, with, possibly, some additional data. For example:

        Score, Level, ID
        45, 2, 0234
        80, 1, 0111
        ...

As in the examples, the field names for the unique identifier may be distinct, but anyway their presence is guaranteed. Therefore, the column names are parameters of the program.

Note that:
- the names of the two files might be different from that of the examples
- the number, the names and the order of the columns might change. The only requirement is that there will always be a unique identifier in both files in order to create a reference from each score to the corresponding employee. 
- the length of the scores file might be less than that of the names file, because some employees might not get a score (for whatever reason).

With these constraints, you should write a python program that uses the above files to produce two more files:

1. a copy of the names file with an additional column, named "Bonus", containing the money the employee will get. This file must contain **only the names present in the scores file**, that is, those getting a bonus. In other words, the length of this file is that of scores.txt while its structure (apart from the additional column) is that of names.txt.

2. produce a fifth file with  the total sum the bonuses and the distribution of prizes, according to the following format:

        Total: 123000
        B0:15000
        C1:25000
        C2:44000
        ...

## Implementation

While writing the code:
- explain clearly the purpose and the input and output of all functions (unless they are extremely obvious)
- when designing a function consider that a general principle to follow is that a function should do just one thing and it should not have side effects (like printing, etc.)
- remember that some specifications might change in the future so decomposing a task into multiple functions allows for an easier management of the possible future management.


