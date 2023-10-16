### PROBLEM ###


You have a map of size NxN with cells of two types -- water ('o') and ground ('.'). All water cells are connected (there is always a path from each water cell to another) and make a water reservoir.
A question is, this reservoir is a Sea or Lake?

The reservoir is called a Lake if there is a path around reservoir using only ground cells. Otherwise, it is a Sea.
Input
Line 1: An integer N for the number rows and columns of map.
Next N lines: A string row[i] that represents i-th row of map. Each line is N characters long.
Output
A single line containing "Lake" if water cells form a Lake, "Sea" otherwise.
Constraints
1 <= N <= 10
Example
Input
4
....
.o..
.oo.
....
Output
Lake



### CODE FOR THE PROBLEM ###


import sys
import math
n = int(input())
a=0
for i in range(n):
    row = input()
    for j in range(len(row)):
        if j==0 or j==len(row)-1:
            if row[j]=="o":
                a+=1
if a==0:
    print("Lake")
else:
    print("Sea")


