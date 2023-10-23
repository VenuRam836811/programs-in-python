### PROBLEM ###


You are on a unlimited grid, you can move in any direction, or wait.
Given the number of turns, you have to print the number of possible positions where you can end.

For example, if the number of turns is 3, the possibilities are :
.........
....3....
...323...
..32123..
.3210123.
..32123..
...323...
....3....
.........

So the number of possible positions at the end is 1+3+5+7+5+3+1 = 25
Input
Line 1: the number of turns nbTurns
Output
The number of possible positions at the end nbPositions
Constraints
0 ≤ nbTurns ≤ 32750
Example
Input
3
Output
25



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n= int(input())
a=1
sum=sum1=0
if n!=0:
    for i in range(1,n+1):
        if i==n:
            sum+=a+2
        sum=sum+a
        sum1=sum1+a
        a=a+2
    print(sum+sum1)
if n==0:
    print("1")



