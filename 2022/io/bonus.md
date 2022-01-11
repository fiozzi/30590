# Bonus pay

At the end of the year a company rewards its employees with a bonus pay
The bonus pay is related to an "activity" score, a number in the range 0-100 that summarizes what the employee has done during the past year. 
If score of employee A is higher than that of employee B, then A will get at least as much as B, maybe more (see below).

The company has decided to give 4 types of bonus: A, B, C and D. Every type corresponds to a fixed bonus which is specified in the model (because it might change from year to year). A is the smaller bonus, D is the higher. Slots and bonuses are defined in a text file, whose format is the following

    A: 0-29: 1000
    B: 30-69: 2000
    C: 70-89: 3000
    D: 90-100: 5000

The scores are computed through an internal assessment at the end of which the direction gets two files:
1) a text file with a list of employees, each one identified through a a unique identifier, with some additional data (for example, first and last name). An example of this file is the file names.txt.
2) a text file containing in each line the unique identifier and a score, with, possibly, some additional data. An example of this file is the  file score.txt

The files the direction receives each year guarantee only that there is a unique correspondence from any line of the scores files to a single line of the identifier files. In particular
- the names of the two files might be different from that of the examples
- the number, the names and the order of the columns might change. The only requirement is that there will always be a unique identifier in both files in order to create a reference from each score to the employee. For example, there might be a file named employees.txt with the following content:

      Name, UniqueID
      John Doe, 0234
      Jane Smith, 0022
      ...
  and a scores.txt file with the following content:

      Score, Level, UniqueID
      45, 2, 0234
      80, 1, 0111
      ...
- the length of the two files in not expected to be equel. The identifier file contains all the employees and its length is, obviously, variable with time. The scores file might contain less lines than the other, because some employees might not get a score (for whatever reason).

The distribution of scores might be such that some slots are underrepresented or even not represented at all (for example, the highest bonus slot might be restricted to the range 95-100 and no employee might not have reached that score).

With these constraints, the CEO wants a python program that uses
- the identifier file
- the score file
- the slot file

to 
1. produce a fourth file with as many lines as the score file, and whose fields are: ID, score and bonus. For example,

        ID, Score, Bonus
        0122, 45, 1000
        0200, 80, 3000
        ...

2. compute the total sum the bonuses will cost and a summary of the distribution of prizes.

If the CEO is satisfied with the outcome, they'll send the file to the administrative offices for the payment. Otherwise, they will change the slot file and run again the program.

## Implementation

While writing the code, consider that:
- The CEO knows how to edit text file, and they're going to do so, to analyze different scenarios. Moreover, they are fine with using a text based interface (i.e., the python Console)
- Your program might undergo an upgrade in the future, with a web interface. Anyway, calculations and text files will remain the same to do as much as you can to separate the content from the appearance
- While the examples provide the current snapshot of the situation, there might be changes in the future. For example, the number of types of bonuses might be reduced to 3. Write the code in such a way to minimize the changes to the structure
- Decompose the program into many consistent units, that is, functions. 


