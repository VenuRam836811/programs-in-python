### PROBLEM ###

Strong Number
Requested files: Strong.java (Download)
Maximum number of files: 5
Type of work: Individual work
Program to check if a given number is a strong number or not is discussed here. A strong number is a number in which the sum of the factorial of the digits is equal to the number itself.
Input & Output Format:
Input consists of one integer.
Output consists of a string. 
If it is true then display "Strong Number" else display "Not a Strong Number".
Sample Input & Output:
145
Strong Number


### CODE FOR THE PROBLEM ###

a=int(input())
a1=a
b=x=0
c=1
while a!=0:
    b=a%10
    a=a//10
    c=1
    for i in range(1,b+1):
        c=c*i
    x+=c
if x==a1:
    print("Strong Number")
else:
    print("Not a Strong Number")
