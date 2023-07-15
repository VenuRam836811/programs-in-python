### PROBLEM ###

Series I
Requested files: Series1.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to generate the following series --- 1,4,9,16,25, .... 
Input format: 
The input containing an integer which denotes 'n' 
Output format: 
Print the series and refer the sample output for formatting
Sample Input :
7
Sample Output:
1 4 9 16 25 36 49 

### CODE FOR THE PROBLEM ###

import math
a=int(input())
for i in range(1,a+1):
    print(int(math.pow(i,2)),end=' ')                                            

