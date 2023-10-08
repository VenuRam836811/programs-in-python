### PROBLEM ###


Background
On board a satellite or spacecraft, a star tracker is an optical device that measures the positions of stars using photocells or a camera.

As the positions of many stars have been measured by astronomers to a high degree of accuracy, a star tracker allows to determine the orientation (or attitude) of the spacecraft with respect to the stars. In order to do this, the star tracker will obtain an image of the stars as input, measure their apparent position in its Field of View (FoV), and identify the stars so their position can be compared with their known absolute position from a star catalog.

Task
Your task is to write (a very simplified) processor that identifies stars (represented by the characters + or x or o and outputs their individual coordinates line by line.

The scanning of the sky is done row by row, starting from coordinate (1,1) in the top left corner of the FoV.
Input
Line 1: An integer n for the number of rows in your FoV.
Next n lines: each line represents a row of what the star tracker sees.

Be careful, there might be some noise in the FoV (for example comet dust), and not everything you see is a star.
Output
Line 1: The coordinates (x,y) of the first detected star.
Line 2: Coordinates of the second detected star.
Line N: Coordinates of the Nth detected star.

Exceptions are:
- if your FoV is filled with #, then you are blinded by a celestial object (for example the moon) and you have to output: BLINDED
- if your FoV does not contain enough valid stars (i.e. less than 1), then you have to output: SEARCH
Constraints
1 ≤ n ≤ 99
0 ≤ len(row) ≤ 1024
Example
Input
1
+
Output
(1,1)


  ### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=b=0
for i in range(n):
    row = input()
    for j in range(len(row)):
        if row[j]=="+" or row[j]=='x' or row[j]=='o':
            print("({},{})".format(j+1,i+1))
            b+=1
        elif j=='#':
            a+=1
if a/len(row)==n:
    print("BLINDED")

    print("SEARCH")

