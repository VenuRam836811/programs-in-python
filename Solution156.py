### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
abcdef
fedcba
02 Test 2
Input
Expected output
abc123
cba123
03 Test 3
Input
Expected output
hi123are559887fine11
ih123era559887enif11
04 Test 4
Input
Expected output
123456789
123456789
05 Test 5
Input
Expected output
a
a
06 Test 6
Input
Expected output
5
5



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
str=""
a=0
for i in s:
    if i.isalpha():
        str+=i
    if i.isdigit():
        print(str[::-1],end="")
        print(i,end="")
        a=1
        str=""
if a==0:
    print(str[::-1])
