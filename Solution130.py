### PROBLEM ###


The program:
Remove the most significant set bit from the given decimal numbers.

INPUT:
Line 1: An integer N for the number of decimal numbers to handle.
Next N lines: A decimal integer num that you need to handle.

OUTPUT:
N lines: The integers that had their most significant set bit removed in decimal format

CONSTRAINTS:
1 ≤ N ≤ 10
1 ≤ num ≤ 2^31

EXAMPLE:
Input
1
500
Output
244
 



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
sum=a=0
for i in range(n):
    num = int(input())
    for i in range(num):
        sum=pow(2,i)
        if sum<=num:
            b=sum 
    print(num-b)
    


