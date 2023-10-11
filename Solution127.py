### PROBLEM ###



The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
1
@-|4|-@
1
02 Test 2
Input
Expected output
3
   /-|10|-\
@-<        >-@
   \-|10|-/
2
03 Test 3
Input
Expected output
1
@-|7|--|18|--@
2
04 Test 4
Input
Expected output
1
@-|20||10|-@
2
05 Test 5
Input
Expected output
3
           /-|8|-\
@-\       /       \-@
   \-|7|-/
2
06 Test 6
Input
Expected output
7
       /-|30|-\
    /-<        >-\
   /   \-|20|-/   \    /-|30|-\
@-<                >--<        >-@
   \   /-|24|-\   /    \-|30|-/
    \-<        >-/
       \-|24|-/
6


### CODE FOR THE PRONLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=0
for i in range(n):
    test = input()
    for i in test:
        if i=='|':
            a+=1
print(a//2)
