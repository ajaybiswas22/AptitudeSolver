# AptitudeSolver

A Python and TKInter based Aptitude Solver.
See the documentation folder for undertanding the working principle.

1. How to add formulas to the database

The db folder contains the database. To add your own formulas, first create a text file, eg. percentage.txt.
To add formulas and the problem definition, use the following style.

X percent of Y : ( X / 100 ) * Y

The LHS part before the colon, is the problem definition. X and Y are variables. The RHS part contains the formula.
Now update x.txt file so that this formula can be referenced.

percentage.txt % of `
percentage.txt percent of `

The first word determines the location and remaining words except " ` " are keywords.

2. Future Work

Currently, keywords based searching is performed. In future, an AI engine will be attached that will substitute over 
keyword based searching.
