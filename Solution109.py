### PROBLEM ###


Billy entered an elevator on floor st. But unfortunately someone before him pulled a prank and pressed n buttons randomly, therefore he will have to wait for the elevator to reach every floor pressed before being able to go to the floor he wants.

Knowing that Billy starts on floor st and that it takes t seconds for the elevator to move from one floor to the next :
Create a code able to calculate the time taken by the elevator to reach each floor pressed.

In this problem we assume the elevator is a sequential machine and follows exactly the order the buttons were pressed!
Input
Line 1 : The starting floor st
Line 2 : t seconds for the elevator to move from one floor to the next
Line 3 : n button pressed
Next n Lines : The floors the elevator must reach (in that order)
Output
Line 1: An integer, the time needed for the elevator to reach the last floor on the list
Constraints
-100 ≤ st ≤ 100
1 ≤ t, n ≤ 100
Example
Input
0
5
3
2
4
5
Output
25



### CODE FOR THE PROBLEM ###


import sys
import math
st = int(input())
t = int(input())
n = int(input())
sum=0
for i in range(n):
    f = int(input())
    if i==0:
        sum+=f
    else:
        sum+=f-sum

m=abs(sum-st)

print(m*t)
