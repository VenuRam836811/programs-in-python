### PROBLEM ###

For a given l-digit long number n, return a number m obtained by raising each digit of n to the power of the length l and replacing it by the last digit (LD) of its power. Let's call m the lth digit power of n.

Examples:
  1-digit long:   2 ➔ 2^1 ➔ 2
  2-digit long:  32 ➔ 3^2, 2^2 ➔ 9, 4 ➔ 94
  3-digit long: 253 ➔ 2^3, 5^3, 3^3 ➔ 8, 125, 27 ➔ 857
Input
Single line: an integer n, with l digit(s)
Output
Single line: an integer, lth digit power of n
Constraints
0 ≤ n
Example
Input
2
Output
2


### CODE FOR THE PROBLEM ###


import math
a=int(input())
b=str(a)
c=len(b)
for i in b:
    v=int(i)
    n=int(math.pow(v,c))
    m=str(n)
    if len(m)==1:
        print(n,end='')
    elif len(m)>1:
        print(m[len(m)-1],end='')
    

