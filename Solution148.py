### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
Codingame
Codingame
eCodingam
meCodinga
ameCoding
gameCodin
ngameCodi
ingameCod
dingameCo
odingameC
Codingame
02 Test 2
Input
Expected output
XP
XP
PX
XP


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input()
str1=''
print(l)
if l==l[::-1]:
    print(l)
else:
    for i in range(len(l)):
        str1=""
        str1+=l[len(l)-1]
        for j in range(len(l)-1):
            str1+=l[j]
        print(str1)
        l=str1
    

