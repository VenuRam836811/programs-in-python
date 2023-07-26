### Program ###

Given a string, can you sum the numbers while excluding any digits that form part of a word?
Input
a string
Output
an integer
Constraints
Example
Input
hi
Output
0

### CODE FOR THE PROBLEM ###

import sys
import math

t = input()
b=0
a=t.split(" ")
for i in a:
    if i.isdigit():
        b+=int(i)
print(b)
