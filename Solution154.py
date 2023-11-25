### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
ABcdE
bcDEf
02 Test 2
Input
Expected output
dooR
EPPs
03 Test 3
Input
Expected output
Hi
iJ
04 Test 4
Input
Expected output
hoLz
IPmA


### CODE FOR THE PROBLEM ###


import sys
import math
s = input()
for i in range(len(s)):
    if s[i].islower() and s[i]!='z':
        c=ord(s[i])-96
        print(chr(c+65),end="")
    if s[i].isupper() and s[i]!='Z':
        v=ord(s[i])-64
        print(chr(v+97),end="")
    if s[i]=='z':
        print("A",end="")
    if s[i]=='Z':
        print("a",end="")
