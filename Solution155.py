### PROBLEM ###


You are given a number N and a list of integers. You must output exactly 2 numbers that are in the list and their sum is equal to N
Input
Line 1: An integer N for the target sum.
Line 2 : An integer L for the length of the list.
Line 3 : A list of space separated integers to look for the target number.
Output
A single line of exactly 2 space separated integers that sum up to N if such exist in the array, N/A otherwise. Smaller number first.
Constraints
-100 <= N <= 100
2 <= array length <= 10
-100 <= array elements <= 100
Example
Input
9
5
1 2 3 4 5
Output
4 5



### CODE FOR THE PROBLEM ###


import sys
import math
n = int(input())
l = int(input())
a=[]
c=0
for i in input().split():
    x = int(i)
    a.append(x)
for i in a:
    b=n-i
    if b in a:
        print(min(i,b),max(i,b))
        break
    else:
        c+=1
if c==len(a):
    print("N/A")
    
