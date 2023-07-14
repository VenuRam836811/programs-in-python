### PROBLEM ###

Sum of Digits
Requested files: Sum.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to find the sum of digits in a given number. Program to find the sum of digits of the given number is discussed here. 
For example, let the input number be 719. The sum of digits of 719 = 7 + 1 + 9 = 17
Input & Output Format:
Input consists of one integer.
Output consists of sum of digits.
Sample Input:
719
Sample Output:
17

### CODE FOR THE PROBLEM ###


def digit(a):
    sum=0
    while(a!=0):
        b=a%10
        sum=sum+b
        a=a//10
    print(int(sum))
a=int(input())
digit(a)
