### PROBLEM ###

Swapping without third variable
Requested files: Swap.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to swap two values without the use of 3rd variable. 

Input format: 

First input: an integer

Second input: an integer 

Output format: 

The output will be integers(swapped values)

Sample Input:

 10

 20

 Sample Output:

 20

 10

### CODE FOR THE PROGRAM ###

a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a)
print(b)
