### PROBLEM ###

The Simple BF language consists of three characters and a single 8-bit value in memory.
+ indicates to increment that value.
- decrements it.
. means output the current ASCII value.

This value cannot underflow or overflow.
If the memory value would become negative, value < 0, output UNDERFLOW.
If the memory value would exceed 8-bit, value > 255, output OVERFLOW.
The value starts at 0.
Input
A string only consisting of characters + - .
Output
The output string of the program if the memory stays within bounds.
Otherwise UNDERFLOW or OVERFLOW.
Constraints
0 < input length < 1024
0 <= memory value < 256
Example
Input
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++.-----------.+.-----------------------.
Output
CODE.


  ### CODE FOR THE PROBLEM ###

import sys
import math
s = input()
w=b=0
SUM=''
for z in s:
    b+=1
   
    if z=='+':
        w+=1
    elif z=='-':
        w-=1
    else:
        w=w
        SUM+=chr(w)
        
if w>255:
    print('OVERFLOW')
elif w<0:
    print('UNDERFLOW')
else:
    print(SUM)
