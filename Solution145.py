### PROBLEM ###


Write a program that will input a proper fraction and display it in its simplest form. If the denominator is zero, then report an error.

Example:
In the second example, the fraction is 2/4
So, the fraction can be further reduced into 1/2.
Input
Line 1: A fraction in the form N / M (space separated), where N and M are integers
Output
The given fraction in the simplest form: N / M
Note: If the denominator is zero, print a line INVALID
Constraints
0<=M,N<=10000
Example
Input
2 / 3
Output
2 / 3



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

f= input()
a=f.split("/")
a1,b1=int(a[0]),int(a[1])
for i in range(1,max(a1,b1)+1):
    if a1%i==0 and b1%i==0:
        a2=a1//i
        b2=b1//i
if b1==0:
    print("INVALID")
else:
    print("{} / {}".format(a2,b2))
