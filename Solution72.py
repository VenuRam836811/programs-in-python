### PROBLEM ###

Pattern III
Requested files: Pattern3.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a Python program to print the given pattern from user-defined values(dynamic values).

Sample input 1:
5
Sample output 1:
*
**
***
****
***** 
Sample input 2:
8
Sample output 2:
*
**
***
****
*****
******
*******
********

### CODE FOR THE PROBLEM ###

a=int(input())
for i in range(1,a+1):
    print("*"*i+" "*(a-1))
