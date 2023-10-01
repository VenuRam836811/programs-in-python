### PROBLEM ###


Given n integers separated by spaces stored in l, you must display all couples of elements where an element is twice its previous one. If there is no couple, output ”NO COUPLE”

Example :
With :
n = 10
l = “7 1 2 5 3 6 -5 -10 8 4”
The output is:
1 2
3 6
-5 -10
Since 2 is the double of 1, 6 is the double of 3 and -10 is the double of -5.
Input
line 1 :  An integer n which is the number of elements in the list l
line 2 :  A string l with n numbers. The numbers are separated by spaces
Output
Each time a number is twice its previous, print one line with the couple of numbers separated by one space. If there is no couple, output ”NO COUPLE”
Constraints
2 ≤ n ≤ 1 000
-10 000 ≤ each number in l ≤ 10 000
Example
Input
10
7 1 2 5 3 6 -5 -10 8 4
Output
1 2
3 6
-5 -10



### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of number in l
l=[]
a=0
for i in input().split():
    x = int(i)
    l.append(x)
for i in range(len(l)):
    if i<len(l)-1:
        for j in range(i+1,i+2):
            if(l[i]*2==l[j]):
                print(l[i],l[j])
                a+=1
if a==0:
    print("NO COUPLE")
    


