### problem ###

Pattern IX
Requested files: Pattern9.python (Download)
Maximum number of files: 5
Type of work: Individual work
Write a Python program to print the given pattern from user-defined values(dynamic values).

Sample input 1:     
5
Sample output 1:
*********
  *******
    *****
      ***
        *
Sample input 2:
8
Sample output 2:

***************
  *************
    ***********
      *********
        *******
          *****
            ***
              *

### CODE FOR THE PROBLEM ###

a=int(input())
for j in range(a):
    print(" "*(j*2)+"*"*(a+a-1-j*2))
        
