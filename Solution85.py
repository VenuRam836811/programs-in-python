### PROBLEM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
727332688568693233
HI DUDE !
02 Test 2
Input
Expected output
7384398332657832696583893280859090766946325841
IT'S AN EASY PUZZLE. :)
03 Test 3
Input
Expected output
666976736986693277694432733977327879843265327673658232407485838432653282796679844146
BELIEVE ME, I'M NOT A LIAR (JUST A ROBOT).
04 Test 4
Input
Expected output
847273833283697884697867693267798576683266693276797871698244327384328779857668328384737676326669326965838932333272858282893285803233325941
THIS SENTENCE COULD BE LONGER, IT WOULD STILL BE EASY ! HURRY UP ! ;)


### CODE FOR THE PROBLEM ###

import sys
import math

str=input()
sum=0
for i in range(int(len(str))):
    if(i%2==0):
        a=str[i:i+2]
        sum=0
        for k in a:
            v=int(k)
            sum=sum*10+v
        print(chr(sum),end='')

