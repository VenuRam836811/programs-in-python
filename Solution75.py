### PROBLEM ###

Pattern VI
Requested files: Pattern6.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a Python program to print the given pattern from user-defined values(dynamic values).

Sample Input 1:
5
Sample output 1:
*****
 ****
  ***
   **
    * 
Sample input 2:
8
Sample output 2:
********
 *******
  ******
   *****
    ****
     ***
      **
       *

### CODE FOR THE PROBLEM ###

a=int(input())
for i in range(a):
    print(" "*i+"*"*(a-i))  
