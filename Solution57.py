### PROBLEM ###

Sum of Positive square elements
Requested files: Pos.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to find the sum of positive square elements in an list:
Input & Output Format:
First Input consists of size of an array
Remaining inputs corresponds to the number of elements based on the size.
Output consists of an integer.
Sample Input:
3
2
4
6
Sample Output:
4


### CODE FOR THE PROBLEM ###

import math
a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
for i in range(a):
    c=math.sqrt(b[i])
    d=int(c)
    if(b[i]!=1):
        if(c==d):
            print(b[i])
