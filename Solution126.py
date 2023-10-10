### PROBLEM ###


Let's start with the factorial function:

Example: 4! = 4 x 3 x 2 x 1 = 24

Here, we define magic factorials by the new rule that for every odd number in the sequence other than n, you have to divide instead of multiply and round only the result.

Example: 5!! = 5 x 4 / 3 x 2 / 1 = 13.333... => 13 (round to nearest integer)

Only 3 and 1 are treated as odd numbers in the sequence (n doesn't count)
Input
Line 1 : An integer N.
Output
Line 1 : An integer X whose result is sought from the magic factorial function of N.
Constraints
3 < n < 50
Example
Input
5
Output
13

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m=1
for i in range(n,1,-1):
    if i==n:
        m*=i
    elif i%2==1:
        m/=i
    elif i%2==0:
        m*=i
print(int(round(m)))



### CODE FOR THE PROBLEM ###


