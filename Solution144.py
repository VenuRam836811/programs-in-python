### PROBLEM ###


Output the factorial of the integer N if N is positive
Input
An integer N to convert.
Output
If the integer provided isn't negative output a factorial of N else output "No negative integers"
Constraints
-100 ≤ N ≤ 100
Example
Input
5
Output
120



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
n = int(input())
if n>=0:
    print(fact(n))
else:
    print("No negative integers")

