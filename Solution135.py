### PROBLEM ###


Help the snake (named python) P to find the Apple A.

What direction should it take? and how many times?
Input
Line 1 : Integer N for the size of the grid
Next N lines : N String s for one line of the grid which may contain P or/and A
Output
Line 1 : LEFT or RIGHT x number of times (separated by a space) or return 0 if no need
Line 2 : UP or DOWN x number of times (separated by a space) or return 0 if no need
Constraints
2 ≤ N ≤ 50
Example
Input
4
P...
....
..A.
....
Output
RIGHT x 2
DOWN x 2



### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
a=b=c=d=0
n = int(input())
for i in range(n):
    str = input()
    for j in range(len(str)):
        if str[j]=="P":
            a=i
            b=j
        elif str[j]=="A":
            c=i
            d=j
if d-b==0 and abs(c-a)!=0:
    print(d-b)
    print("DOWN x",(c-a))
elif (b-d)!=0 and (c-a)!=0:
    print("RIGHT x",(c-a))
    print("DOWN x",d-a)
elif c-a==0 and (b-d)!=0:
    print("RIGHT x",abs(b-d))
    print("0")





