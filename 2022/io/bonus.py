"""
Bonus pay

At the end of the year a company rewards its employees with a bonus pay
The bonus pay is related to an "activity" score, a number in the range 0-100
that summarizes what the employee has done during the past year. 
The higher the score, the higher the bonus.

The amount the company has budgeted for the bonus is variable, call it B. 
Each employee is going to get a fraction of B.
The company direction has decided to use a score slots system. 
They must set up an arbitrary number of slots to cover the entire score range. 
Each slot is then assigned a fraction of B and each employee in that slot 
will receive the same quota as the other employess in the same slot.
For example, if the slots are
0-29 with 30% of B
30-79 with 60% of B
80-100 with 10% of B
and if there are 15 employees whose score is in the range 0-29, 
then each of them will get (30% of B)/15, which amounts to 2% of B.

The accounting dept uses Microsoft Excel and has exported two files:
1) names.txt is a text file with ID, First Name, Last Name 
of each employee (all strings)
2) IDscores.txt is a text file with ID, Score (string and number)
They want to receive from the direction a file with

ID, First Name, Last Name, Score, PercBonus

where PercBonus is a decimal number in the range 0-100 
(actually, 100 sould imply all other perecentages are 0, which sounds 
impossible but, who knows ...)

Note that IDScores.txt might contain less lines than names.txt, since 
not every employee, for various reasons, is eligible for the bonus. 
Moreover, the distribution of scores is unpredicatble and some entire 
ranges might be missing. For example, if the slots are 
0-49 with 30% of B
50-100 with 70% of B
and only 6 employees got a positive score, all equal to 20, 
then 30% of B will be equally shared by the 6 employees, each one getting 5%.
In this case, the company will use the rest of the budgeted amount for
other investments.

The direction wants a python program to let them "experiment" with 
different bonus slots, given an assigned score table (that is, that 
contained in IDScores.txt)

The program takes the names as paramters:
1) the file of the names, defaults to names.txt
2) the file of the scores, defaults to scores.txt
3) a distrubition in the form of a dictionary (see below)
4) the (1-based) number of the column with the identifier in the names file, 
defaults to 1
5) the (1-based) number of the column with the identifier in the scores file,
defaults to 1
6) the (1-based) number of the column with the score in the scores file,
defaults to 2

Every item in the dictionary is {low-endpoint: perc-of-B}. For example
the distribution

0-29 with 30% of B
30-79 with 60% of B
80-100 with 10% of B

is described by the dict 

{'0':30, '30':60, '80':10}

All parameters are taken from a config file.

The output of the program is a text file in the format

ID, First Name, Last Name, Score, PercBonus

where every line gives the percentage for those whose ID appears in
IDScores.txt.

All the data are subject to change at any time so the script should not 
assume anything by default. In particular, the number, the names and the order
of the columns in both files might change. The only requirement is that there
will be a unique identifier in both files to create a reference from one table 
to another. For example, the file names.txt might be like:
Name, UniqueID
John Doe, 0234
Jane Smith, 0022
...
and the IDScores might be
Score, Level, UniqueID
45, 2, 0234
80, 1, 0111
...

two be On the contrary, the format of the files is
stable (so you can assumeThe number of employees is given by the lines 
in the names.txt file.

"""