### PROBLEM ###


Depending on the input, return lines of numbers as below.
Input
3
Output
123
21
1
Constraints
Example
Input
2
Output
12
1



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    if i%2==0:
        for j in range(1,n+1-i):
            print(j,end="")
    else:
        for j in range(n-i,0,-1):
            print(j,end="")
    print()
