### PROBLEM ###

7H3 M345UR3 0F 1N73LL163NC3 15 7H3 481L17Y 70 CH4N63
translates/decodes to
THE MEASURE OF INTELLIGENCE IS THE ABILITY TO CHANGE
Let this Albert Einstein's quote guide you in translating the given words/phrases.
~ ~ ~ ~ ~
Background for your amusement (NOT needed to solve this Clash):
https://www.quora.com/Why-can-we-read-1N73LL1G3NC3-15-7H3-4B1L17Y-70-4D4P7-70-CH4NG3
https://www.amazon.com/1n73ll1g3nc3-4b1l17y-4d4p7-ch4ng3-Sweatshirt/dp/B08FTSZMLV
Input
Line 1: An integer, number of lines to follow
next n Lines: A string, a word/phrase (wordOrPhrase) to translate/decode
Output
n Lines: Each wordOrPhrase translated/decoded
Constraints
Example
Input
3
7H3 M345UR3 0F 1N73LL163NC3 15 7H3 481L17Y 70 CH4N63
48L3 70 637 4 W0RD 1N 3D63W153
0R4N63 H0R535H03 847
Output
THE MEASURE OF INTELLIGENCE IS THE ABILITY TO CHANGE
ABLE TO GET A WORD IN EDGEWISE
ORANGE HORSESHOE BAT

### CODE FOR THE PROBLEM ###


import sys
import math

# 7H3 M345UR3 0F 1N73LL163NC3 15 7H3 481L17Y 70 CH4N63
# translates/decodes to
# THE MEASURE OF INTELLIGENCE IS THE ABILITY TO CHANGE

n = int(input())
for i in range(n):
    wo= input()
    for j in wo:
        if j=='7':
            print("T",end='')
        elif j=='3':
            print("E",end='')
        elif j=='4':
            print("A",end='')
        elif j=='5':
            print("S",end='')
        elif j=='0':
            print("O",end='')
        elif j=='1':
            print("I",end='')
        elif j=='6':
            print("G",end='')
        elif j=='8':
            print("B",end='')
        else:
            print(j,end='')
    print()



