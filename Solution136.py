### PROBLEM ###


For all numbers less or equal to n, you must return the difference between the sum of all the numbers divisible by 3 and the sum of even numbers.
Input
one integer n
Output
one integer : the difference between the two sums.
Constraints
0 <= n <= 100000
Example
Input
5
Output
-3


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=b=0
for i in range(n+1):
    if i%3==0:
        a+=i
    if i%2==0:
        b+=i
print(a-b)
