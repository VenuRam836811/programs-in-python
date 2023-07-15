### PROBLEM ###

Sum of natural Numbers
Requested files: Sum.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to find the sum of first N natural numbers.
Input & Output Format:
Input consists of one integer.
Output consists of a integer.
Sample Input & Output:
5
15

### CODE FOR THE PROBLEM ###

 def sum(a):
    if a==0 or a==1:
        return a
    else:
        return a+sum(a-1)
a=int(input())
print(sum(a)) 
