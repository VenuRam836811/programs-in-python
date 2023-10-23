### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
1
23:59
00:00
02 Test 2
Input
Expected output
5
11:23
11:28
03 Test 3
Input
Expected output
50
12:59
13:49
04 Test 4
Input
Expected output
21
22:39
23:00



### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s= input().split(":")
a=int(s[0])
b=int(s[1])
if b+n==60 and (a+1)==24:
        print("00:00")
elif b+n<60:
    if a<24:
        print(str(a)+":"+str(b+n))
elif b+n>60:
    a+=1
    c=b+n-60
    if a<24:
        print(str(a)+":"+str(c))
elif b+n==60 and (a+1)<24:
    print(str(a+1)+":"+"00")



