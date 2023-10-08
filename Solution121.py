### PROBLEM ###


You are given a sequence of N positive integers.
You have to print this sequence after a left shift (the first element becomes the last one, the second becomes the first, the third becomes the second, ...).
Input
Line 1: N, the number of elements
Line 2: N positive integers lower than 1 000 000, the elements of the sequence
Output
One line containing exactly N numbers : the sequence after being shifted
Constraints
2 ≤ N ≤ 100
Example
Input
3
3 1 2
Output
1 2 3


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l=[]
for i in input().split():
    v = int(i)
    l.append(v)
for i in range(1,n):
    print(l[i],end=' ')
print(l[0])
    

