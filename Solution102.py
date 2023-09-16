### PROBLEM ###

Calculate the geometric mean of inputs a and b. The geometric mean of two numbers is the square root of a * b.
Input
Line 1: An integer a
Line 2: An integer b
Output
Line 1: An integer c, the geometric mean of a and b
Constraints
a > 0
b > 0
c is guaranteed to be a square number
Example
Input
2
8
Output
4


### CODE FOR THE PROBLEM ###

import math
a=int(input())
b=int(input())
print(int(math.sqrt(a*b)))
