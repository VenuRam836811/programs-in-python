### PROBLEM ###


Greatest of two numbers
Requested files: Compare.java (Download)
Maximum number of files: 5
Type of work: Individual work
Get two integers a and b from the user and write a program to relate 2 integers as equal to, less than or greater than. 

Input format: 

Input consist of 2 integers 

The first input corresponds to the first number(a) 

The second input corresponds to the second number(b) 

Output format: 

If the first number is equal to the second number, print "a is equal to b". 

Otherwise, print "a greater than b" or "a less than b"

Sample Input: 

17

12

Sample Output: 

17 greater than 12


### CODE FOR THE PROBLEM ###


#import math
a=int(input())
b=int(input())
c=max(a,b)
d=min(a,b)
print("{} greater than {}".format(c,d))
