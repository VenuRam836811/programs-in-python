### PROBLEM ###


You have to find the n-th term of arithmetic progression.
A is the first term of the arithmetic progression.
D is the common difference of the arithmetic progression.
'N' stands for the term number
Input
Line 1 A is a positive integer.
Line 2 D is a positive integer.
Line 3 N is a positive integer and stand for term number.
Output
Output the n-th term of arithmetic progression
Constraints
1<=A<=100000
1<=D<=100000
1<=N<=100000
Example
Input
1
2
1
Output
1


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
d = int(input())
n = int(input())

print(int((n-1)*d+a))
