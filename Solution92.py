### PROBLEM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
678
7
02 Test 2
Input
Expected output
9999
9
03 Test 3
Input
Expected output
123
2
04 Test 4
Input
Expected output
145
3
05 Test 5
Input
Expected output
190
3

### CODE FOR THE PROBLEM ###

import sys
import math
a=int(input())
sum=0
b=str(a)
c=len(b)
while a!=0:
    m=a%10
    sum+=m
    a//=10
print(sum//c)
