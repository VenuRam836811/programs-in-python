### PROBLEM ###

Print each prime P <= N P times
Input
Line 1: N
Output
Line 1: String representing the sequence
Constraints
2 <= N <= 50
Example
Input
3
Output
22333

### CODE FOR THE PROBLEM ###

import sys
import math
n = int(input())
a=0
for i in range(2,n+1):
    a=0
    for j in range(2,i+1):
        if(i%j==0):
            a+=1
    if(a==1):
        for j in range(i):
            print(i,end='')
