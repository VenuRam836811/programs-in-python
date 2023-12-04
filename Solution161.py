### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
00000 AAAAA xxxxx
01110 BBBBB xxxxx
01110 CCCCC xxxxx
01110 DDDDD xxxxx
00000 EEEEE XXXXX
AAAAA
BxxxB
CxxxC
DxxxD
EEEEE
02 Test 2
Input
Expected output
00000 First Error
00000 Bravo Avoid
00000 Third These
00000 Delta Other
00000 Fifth Words
First
Bravo
Third
Delta
Fifth



### CODE FOR THE PROBLEM ###


import sys
import math
for i in range(5):
    line = input().split(" ")
    a=line[0]
    b=line[1]
    c=line[2]
    for j in range(len(a)):
        if a[j]=='0':
            print(b[j],end="")
        if a[j]=='1':
            print(c[j],end="")
    print()
