### PROBLEM ###

LCM of two numbers
Requested files: Lcm.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to find LCM of two numbers is discussed here. Two numbers are obtained as input and the prime factors of both the numbers are found. The product of the union of prime factors of both the numbers gives the LCM of the two numbers.
Input & Output Format:
Input consists of two integers.
Output consists of the lcm of two numbers.
Sample Input:
5
30
Sample Output:
LCM of 5 and 30 is 30

### code for the problem ###

a=int(input())
b=int(input())
c=min(a,b)
d=0
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        d=i
z=int((a*b)/d)
print("LCM of {} and {} is {}".format(a,b,z))
