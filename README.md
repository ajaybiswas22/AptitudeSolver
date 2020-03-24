# AptitudeSolver

A Python and TKInter based Aptitude Solver.
See the documentation folder for undertanding the working principle.

1. How to add formulas to the database

The db folder contains the database. To add your own formulas, first create a text file, eg. percentage.txt.
To add formulas and the problem definition, use the following style (without quotes).

"X percent of Y : ( X / 100 ) * Y"

The LHS part before the colon, is the problem definition. X and Y are variables. The RHS part contains the formula.
Now update x.txt file so that this formula can be referenced. Use the following style (without quotes).

"percentage.txt % of \`"
"percentage.txt percent of \`"

The first word determines the location and remaining words except " \` " are keywords.

2. How to run the program

Run main.py file. A GUI will open. There is a text box where you can enter your problems. Example

"10 percent of 100"

You can provide options in 1,2,3,4 box. Press calculate to calculate result.
You can also check value of some constants like value of pi.

"pi ="

If you haven't provided any choice then the program will select choice 1.

3. Future Work

Currently, keywords based searching is performed. In future, an AI engine will be attached that will substitute over 
keyword based searching.
