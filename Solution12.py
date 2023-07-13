### PROBLEM ###

Power of a Number
Requested files: Pow.java (Download)
Maximum number of files: 5
Type of work: Individual work
pow() function is used to calculate the power of any base and it is defined in math header file. Write a program to read X as the base and N as the power and calculate the result (X^N - X to the power of N). 

Input format: 

The first line containing integer denotes the base(X) 

The second line containing integer denotes the power(N) 

Output format: 

Print the power of a number

Sample Input:

 2

 3

 Sample Output:

 8



### CODE FOR THE PROBLEM ###

import math
def power(a,b):
    print(int(math.pow(a,b)))
a=int(input())
b=int(input())
power(a,b)
