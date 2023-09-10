### PROBLEM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
2 4 6
-12
02 Test 2
Input
Expected output
1 3 5
9
03 Test 3
Input
Expected output
8 10 9 7
-2
04 Test 4
Input
Expected output
810 494 948 362 482 687 617 25 656 737 938 326 563 550 699 918 135 176 107 393 324 262 515 319 477 627 575 237 847 578
-264


### CODE FOR THE PROBELM ###

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input()
sum=0
a=l.split(" ")
for i in a:
    b=int(i)
    if(b%2==0):
        sum-=b
    else:
        sum+=b
print(sum)
