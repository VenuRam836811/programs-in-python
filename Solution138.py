### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
I have 0 chocolate and 1 biskits
I have Buzz chocolate and Lightning biskits
02 Test 2
Input
Expected output
I have 1 chocolate and 3 biskits
I have Lightning chocolate and Lightning biskits
03 Test 3
Input
Expected output
I have 42 chocolate and 64 biskits
I have Buzz chocolate and Buzz biskits
04 Test 4
Input
Expected output
1 orange, 2 apples, 3 lemon, 4 melon
Lightning orange, Buzz apples, Lightning lemon, Buzz melon
05 Test 5
Input
Expected output
Simple message
Simple message



### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m= input()
str=""
m=m.split(" ")
for i in m:
    if i.isdigit():
        v=int(i)
        if v%2==0:
            str+="Buzz "
        else:
           str+="Lightning "
    elif i.isalpha():
        str+=i+" "
    else:
       str+=i+" "
print(str[:-1])


   

