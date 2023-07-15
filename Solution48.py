### PROBLEM ###

Series II
Requested files: Series2.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to generate the following series --- 6,11,21,36,56,... 
Input format: 
The input containing an integer which denotes 'n' 
Output format: 
Print the series and refer the sample output for formatting.
Sample Input:
5
Sample Output:
6 11 21 36 56 

### CODE FOR THE PROBLEM ###

a=int(input())
a1=a
b=a+1
c=1
print(b,end=' ')
for i in range(1,a):
    b=b+a
    a=a1+a
    print(b,end=' ')                                            
