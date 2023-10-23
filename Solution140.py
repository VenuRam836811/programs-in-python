### PROBLEM ###


Given a message, print out the words alternately in n separate lines.
Input
Line 1: An interger n represents the number of lines needed to be seperated.
Line 2: A string.
Output
n distinct lines.
Constraints
2 <= n <= 10
1 ≤ Length of the string ≤ 256
Example
Input
2
This If is you not are a reading very this good then way you to have hide done a it message. wrong.
Output
This is not a very good way to hide a message.
If you are reading this then you have done it wrong.



### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n= int(input())
str=""
m= input().split(" ")
for i in range(n):
    for j in range(i,len(m),n):
       str+=m[j]+" "
    print(str[:-1])
    str=""
    


