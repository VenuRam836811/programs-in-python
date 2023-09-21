### PROBLEM ###


 	Goal
You are given a "marble run": a table of bars which will guide a marble during its fall.
When a marble falls on a "\" bar, it rolls on the right. When it falls on a "/" bar, it rolls on the left.
The marble has no inertia. That is, it will fall vertically if not on a bar.
You are given the column at which the marble enters the run. Find out on which column it will be at the end of the run!
It is guaranteed that the marble will stay inside the run, and that it will not be blocked by the bars. That is, a whitespace is always present on left of "/" and on right of "\".
Input
Line 1: Three space-separated integers H, W and x. H is the height of the marble run. W is its width. x is the column where the marble starts (between 0 and W-1).
Next H Lines: string Row of length W composed of " ", "\" or "/" representing a row of the run
Output
Line 1: Column in which the marble will finish the run (between 0 and W-1)
Constraints
0 ≤ H < 100
0 ≤ W < 100
0 ≤ x < W
Example
Input
6 8 0
\      /
 \    / 
   /\   
  /  \  
       /
\     / 
Output
1


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# h: height of the marble run
# w: width of the marble run
# x: column where the marble starts
h, w, x = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    if row[x]=='/':
        x=x-1
    elif row[x]!=' ':
        x=x+1
print(x)

     
