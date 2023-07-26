### PROGRAM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
4
2
3
4 6 8
4 2 1
02 Test 2
Input
Expected output
81
3
4
81 84 87 90
81 27 9 3
03 Test 3
Input
Expected output
10
1
3
10 11 12
10 10 10
04 Test 4
Input
Expected output
27
3
3
27 30 33
27 9 3

### CODE FOR THE PROGRAM ###

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
z=l
m = int(input())
n = int(input())
print(l,end=" ")
for i in range(n-1):
    print(l+m,end='')
    if(i<n-2):
        print(" ",end='')
        l=l+m
print()
print(z,end=" ")
for i in range(n-1):
    print(int(z/m),end='')
    if(i<n-2):
        print(" ",end='')
        z=z/m



