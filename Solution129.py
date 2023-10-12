### PROBLEM ###


You have 3 integers, a b c, separated by spaces in a single input line.
The last value c could be the result of an operation - + * / between a and b in that order. The / operator should return only the integer part of the division.
If there is no operation linking a,b and c then print error.
You should print all the valid symbols if there is more than one, following the order indicated above and separated by space.
For example: for 7 0 7, the output is -space+.
Input
Line 1: 3 integers a b c separated by spaces.
Output
Line 1 : a string with the valid symbols - + * / separated by spaces (if there is more than one) or the string error.
Constraints
0 ≤ a ≤ 10000
0 ≤ b ≤ 10000
0 ≤ c ≤ 10000
Example
Input
127 45 82
Output
-


### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l=input().split(" ")
a=0
str=""
try:
    if int(l[0])-int(l[1])==int(l[2]):
        str+="-"+" "
        a=1
    if int(l[0])+int(l[1])==int(l[2]):
        str+="+"+" "
        a=1
    if int(l[0])*int(l[1])==int(l[2]):
        str+="*"+" "
        a=1
    if int(l[0])//int(l[1])==int(l[2]):
        str+="/"+" "
        a=1
finally:
    if a==0:
        print("error")
    else:
        print(str[:-1])


