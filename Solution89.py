### PROBLEM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
6
360
02 Test 2
Input
Expected output
7
2520
03 Test 3
Input
Expected output
8
20160
04 Test 4
Input
Expected output
16
10461394944000


### CODE FOR THE PROBLEM ###

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
sum=1
for i in range(1,a+1):
    sum*=i
print(int(sum*0.5))
