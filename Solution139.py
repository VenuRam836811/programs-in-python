### PROBLEM ###


You must output the highest prime number from the given numbers
Input
Line 1: An integer L
Line 2: L integers N separated by spaces
Output
Line 1 : A single line containing the highest prime number in the list.
-1 if there is no prime number
Constraints
1 <= L <= 500
1 <= N <= 1000
Example
Input
10
1 2 3 4 5 6 7 8 9 10
Output
7



### CODE FOR THE PROBLEM ###


import sys
import math
l = int(input())
a=[]
c=0
for i in input().split():
    n = int(i)
    b=0
    for j in range(2,n):
        if n%j==0:
            b+=1
    if b==0:
        c+=1
        a.append(n)
a.sort()
if c==0:
    print("-1")
else:   
    print(a[len(a)-1])



