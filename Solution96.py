### PROBLEM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
John has a cat and a dog
John has a cat and dog
02 Test 2
Input
Expected output
Billy likes to watch soccer and likes to watch basketball
Billy likes to watch soccer and basketball
03 Test 3
Input
Expected output
Bob is hungry and is thirsty
Bob is hungry and thirsty
04 Test 4
Input
Expected output
It is cool that Bob plays basketball and plays hockey
It is cool that Bob plays basketball and hockey


### CODE FOR THE PROBLEM ###

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s=input()
a=[]
s=s.split(" ")
for i in s:
    if i not in a:
        a.append(i)
for i in range(0,len(a)):
    print(a[i],end='')
    if i<len(a)-1:
        print(" ",end='')

