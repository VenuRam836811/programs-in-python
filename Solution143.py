### PROBLEM ###


You are given n integers separated by space. For each element (integer), you must output the product of every other element than the current element. This must be done in order ( 1st number in output should be the product of every integer provided except the 1st, etc., )

Example:

Input :
4
1 2 3 4

Thought process :

For 1 : 2*3*4 = 24
For 2 : 1*3*4 = 12
For 3 : 1*2*4 = 8
For 4 : 1*2*3 = 6

Output :
2 0 0
Input
Line 1: An integer n declaring the amount of elements in the next line.
Line 2: n integers separated by spaces.
Output
Line 1: n product of every element except one (ordered by the index of the excluded element), separated by spaces.
Constraints
Every integer provided in line 2 is unique.
At least 2 integers in second line, n ≥ 2.
Output integers fit in 64-bit signed int type.
Example
Input
4
1 2 3 4
Output
24 12 8 6


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
x=[]
a=1
str1=""
for i in input().split():
    x.append(int(i))
for i in range(len(x)):
    a=1
    for j in range(len(x)):
        if i!=j:
            a*=x[j]
    str1+=str(a)+" "
print(str1[:-1])


