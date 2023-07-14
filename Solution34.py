### PROBLEM ###


Factorial
Requested files: Factorial.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to determine whether n is a factorial number or not. A factorial number is a number that is a factorial of another number.
Input Format:
Input consists of a single integer which corresponds to n.
Output Format:
Output consists of a string - “yes” or “no”
Sample Input 1
6
Sample Output 1
yes
Sample Input 2
12
Sample Output 2
no

### CODE FOR THE PROBLEM ###

a=int(input())
b=1
for i in range(1,a):
    b=b*i
    if b==a:
        break
if b==a:
    print("yes")
else:
    print("no")
