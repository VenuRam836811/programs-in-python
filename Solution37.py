### PROBLEM ###

Harshard Number
Requested files: Harshard.java (Download)
Maximum number of files: 5
Type of work: Individual work
Program to check whether a number is a Harshad number or not (Niven number) is discussed here. Harshad Number is an integer that is divisible by the sum of its digits.
Input format:
Input consists of 1 integer.
If the given number is Harshad Number display Harshad Number or display Not Harshad Number.
Sample Input:
1729
Sample Output:
Harshad Number

### CODE FOR THE PROBLEM ###

a=int(input())
sum=0
while a!=0:
    b=a%10
    sum+=b
    a=a//10
if a%sum==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
