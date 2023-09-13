### PROBLEM ###

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
6
..........
...####...
...#..#...
...#..#...
...####...
..........
16
02 Test 2
Input
Expected output
7
...........
...........
...#####...
...#...#...
...#...#...
...#####...
...........
20
03 Test 3
Input
Expected output
9
##########
#........#
#........#
#........#
#........#
#........#
#........#
#........#
##########
90
04 Test 4
Input
Expected output
4
....
.##.
.##.
.##.
6
05 Test 5
Input
Expected output
1
#############
13
06 Test 6
Input
Expected output
1
#
1
07 Test 7
Input
Expected output
37
......................................
......................................
...........####################.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........#..................#.......
...........####################.......
......................................
......................................
......................................
......................................
620
08 Test 8
Input
Expected output
98
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
.....############################################################################################...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....#..........................................................................................#...
.....############################################################################################...
....................................................................................................
....................................................................................................
....................................................................................................
8372



### CODE FOR THE PROBLEM ###

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=b=0
for i in range(n):
    line = input()
    if "#" in line:
        a+=1
        b=0
        for j in line:
            if j=='#':
                b+=1
print(a*b)


