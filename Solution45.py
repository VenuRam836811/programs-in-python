### PROBLEM ###

Reverse a Number
Requested files: Reverse.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write program to reverse a number is discussed here. We can reverse a number using loop and arithmetic operators in both iterative and recursive approaches. 
Input & Output Format:
Input consists of a integer.
Output consists of reversed input.
Sample Input: 
13579
Sample Output: 
97531

### CODE FOR THE PROBLEM ###

n=int(input())
a=b=0
while n!=0:
    b=n%10
    a=a*10+b
    n=n//10
print(a)
