### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
1 1 2 1 3 1 4 1
ABCD
02 Test 2
Input
Expected output
16 7
PPPPPPP
03 Test 3
Input
Expected output
8 1 5 1 12 2 15 1 23 1 15 1 18 1 12 1 4 1
HELLOWORLD
04 Test 4
Input
Expected output
9 1 12 1 9 1 23 0 11 1 5 1 4 1 21 1 3 1 11 1 19 1 4 1 15 1 25 1 15 1 21 1 12 1 9 1 11 1 5 1 20 1 8 1 5 1 7 0 13 1 20 1 15 1 15 1 9 0
ILIKEDUCKSDOYOULIKETHEMTOO



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a= input().split(" ")
for i in range(len(a)):
    if i%2==0:
        for j in range(int(a[i+1])):
            print(chr(64+int(a[i])),end="")

