### PROBLEM ###


The greatest common divisor (GCD) of two integers, which are not all zero, is the largest positive integer that divides each of the integers.


Compute the greatest common divisor of |N|to the power of|M| and |M|to the power of|N| where N and M are given integers.

Note: 0 power 0 equals 1
Input
Line 1 : An integer N
Line 2 : An integer M
Output
Line1 : The greatest common divisor of |M|^|N| and |N|^|M|
Constraints
-10≤ N ≤10
-10≤ M ≤ 10
Example
Input
2
6
Output
4


### CODE FOR THE  PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = abs(int(input()))
m = abs(int(input()))
k=0
a=min(n**m,m**n)
for i in range(1,a+1):
    if((n**m)%i==0 and (m**n)%i==0):
        k=i


print(k)
