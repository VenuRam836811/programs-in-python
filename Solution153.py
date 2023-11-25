### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
mIcHEl_lOUIs seRieUX
Michel-Louis SERIEUX
02 Test 2
Input
Expected output
ALEXANDRE buni
Alexandre BUNI
03 Test 3
Input
Expected output
pHiLiPe CARI
Philipe CARI
04 Test 4
Input
Expected output
Tristan BON
Tristan BON



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

name = input().split(" ")
for i in range(2):
    if i==0:
        print(name[0].capitalize(),end=" ")
    else:
        print(name[i].upper())


