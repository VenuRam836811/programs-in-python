### PROBLEM ###


You want to make a 3 digit password, but you have to following rules:
The first digit must be between 0 and a.
The second digit must be between 0 and b.
The third digit must be between 0 and c.
In how many different ways can you create your password?
Input
3 space-separated integers a, b, c.
Output
The number of different ways you can create your password.
Constraints
0 <= a, b, c <= 9
Example
Input
6 6 4
Output
245


### CODE FOR THE PROBLEM ###


import sys
import math

a, b, c = [int(i) for i in input().split()]

print((a+1)*(b+1)*(c+1))
