### PROBLEM ###

Series III
Requested files: Series3.PY (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to generate the first n terms in the series --- 3, 9, 27, 81,...,... 
Input format: 
The input containing an integer which denotes 'n' 
Output format: 
Print the series and refer the sample output for formatting
Sample Input & Output:
5
3 9 27 81 243

### CODE FOR THE PROBLEM ###

import math
a=int(input())
b=3
for i in range(1,a+1):
    c=math.pow(b,i)
    print(int(c),end=' ')                                            
