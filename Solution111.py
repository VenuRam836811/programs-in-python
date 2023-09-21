### PROBLEM ###


Given a 9x9 sudoku puzzle, return the sum of the missing numbers. For a sudoku puzzle, each row, column and box must have the numbers 1-9.
Input
Line 1: A string <n> representing the number of lines.
Other lines: The rows of the sudoku board. Each row will contain the numbers 0-9. Note: 0 indicates an unsolved entry.
Output
the sum of unsolved numbers.
Constraints
n = 9
Example
Input
9
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
Output
246


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a='123456789'
b=405
for i in range(n):
    row = input()
    for j in row:
        if j in a:
            v=int(j)
            b=b-v
print(b)


