### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
6
0 1
1 2
2 4
4 8
8 16
16 32
0
4
32
256
2048
16384
02 Test 2
Input
Expected output
8
84 10000
96 8800
99 7300
82 5100
42 2000
70 600
9 1300
85 5000
8400000000
7434240000
5275710000
2132820000
168000000
25200000
15210000
2125000000



### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    m, c = input().split(" ")
    a=int(m)
    b=int(c)
    c=pow(b,2)*a
    print(int(c))
    
