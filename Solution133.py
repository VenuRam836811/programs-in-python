### PROBLEM ###


Older phones didn't have touchscreens, so writing messages was done on a keypad.
Today, this system is but a relic of the past, but let's use it once more to encode small messages!

The keypad we will be using is the following:
- '2' for ABC
- '3' for DEF
- '4' for GHI
- '5' for JKL
- '6' for MNO
- '7' for PQRS
- '8' for TUV
- '9' for WXYZ

We don't want the digits in the original message to be mixed up with the digits we use to represent the letters.
As such, the digits already used in our system will all be replaced by '_' (underscore).
We don't use '0' and '1' so these two don't need to be changed.
All the other characters (spaces, punctuation, etc) must remain unchanged.
Uppercase and lowercase letters are treated the same.

You'll receive a message as a string S and will need to print out its encoded version.
Input
Line 1: The string S to encode.
Output
Line 1: The encoded string S.
Constraints
0 < S length < 256
Example
Input
Hello World
Output
43556 96753


### CODE FOR THE PROBLEM ###


import sys
import math
s = input().upper()
str=""
for i in s:
    if i in "ABC":
        str+="2"
    elif i in "DEF":
        str+="3"
    elif i in "GHI":
        str+="4"
    elif i in "JKL":
        str+="5"
    elif i in "MNO":
        str+="6"
    elif i in "PQRS":
        str+="7"
    elif i in "TUV":
        str+="8"
    elif i in "WXYZ":
        str+="9"
    elif i in "25638749":
        str+="_"
    else:
        str+=i
print(str)
