### PROBLEM ###


To get optimal pleasure watching TV or monitors, some manufacturers suggest an horizontal visibility angle between 30 to 40° from the couch.

Given the screen width and height, and the coef for the recommended distance, you have to calculate the best distance from the screen : multiply the screen diagonal by the coef.
Input
Line 1 : two space separated floats, respectively the screen width and height,
Line 2 : one float, the coef.
Output
Line 1 : the best distance from the screen, rounded integer.
Constraints
4 ≤ width ≤ 190 cm
3 ≤ height ≤ 106 cm
1.3 ≤ coef ≤ 1.7
Example
Input
4.0 3.0
1.6
Output
8



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [float(i) for i in input().split()]
coef = float(input())
a=math.sqrt(width**2+height**2)
b=round(coef*a)
print(b)
