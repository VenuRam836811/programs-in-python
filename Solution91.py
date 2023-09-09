### PROBLEM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
CodinGame
cOdInGaMe
02 Test 2
Input
Expected output
IYouHeIs
IyOuHeIs
03 Test 3
Input
Expected output
quitJOKINGgetSERIOUS
QuItJoKiNgGeTsErIoUs
04 Test 4
Input
Expected output
kjhkshuuiuhlkrgthhkugsuhkdjfksjhgdfkjghkjskjkjg
kJhKsHuUiUhLkRgThHkUgSuHkDjFkSjHgDfKjGhKjSkJkJg

### CODE FOR THE PROBLEM ###

import sys
import math
s = input()
a=len(s)
if a%2==0:
    for i in range(a):
        if i%2==0:
            b=s[i]
            print(b.upper(),end='')
        else:
            b=s[i]
            print(b.lower(),end='')
else:
    for i in range(a):
        if i%2==1:
            b=s[i]
            print(b.upper(),end='')
        else:
            b=s[i]
            print(b.lower(),end='')


