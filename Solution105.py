### PROBLEM ###

Given an integer N, return the length of the longest sequence containing the same digit.
Input
An integer N.
Output
A single line containing the integer K which is the length of the longest sequence of repeated digits.
Constraints
2 ≤ N ≤ 100000000
Example
Input
111
Output
3


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=str(n)
b=c=0
for i in range(len(a)):
    if i<len(a)-1:
        if a[i]==a[i+1]:
            b+=1
        elif a[i]!=a[i+1]:
            c+=1
print(len(a)-c)
