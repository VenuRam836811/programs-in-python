### PROBLEM ###

Series IV
Requested files: Series4.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to generate the following series --- 0.5,1.5,4.5,13.5,...
Input format: 
The input containing an integer which denotes 'n' 
Output format: 
Print the series and refer the sample output for formatting.
Sample Input & Output:
5
0.5 1.5 4.5 13.5 40.5 

### CODE FOR THE PROBLEM ###

a=int(input())
b=0.5
print(b,end=' ')
for i in range(1,a):
    b=b*3
    print(b,end=' ')                                            
