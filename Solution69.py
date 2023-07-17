### PROBLEM ###

Series V
Requested files: Series5.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to generate the following series --- 121,225,361,... 
Input format: 
The input containing an integer which denotes 'n' 
Output format: 
Print the series and refer the sample output for formatting.
Sample Input & Output:
5
121 225 361 529 729 


### CODE FOR THE PROBLEM ###

import math
a=int(input())
b=11
for i in range(a):
    c=math.pow(b,2)
    b=b+4
    print(int(c),end=' ')
