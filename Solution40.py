### PROBLEM ###

Perfect Number
Requested files: Perfect.java (Download)
Maximum number of files: 5
Type of work: Individual work
Program to check whether a given number is a perfect number or not is discussed here. A perfect number is a number which is equal to the sum of its proper positive divisors.
For example, 6 is a perfect number.
The divisors of 6 are 1, 2 and 3.
1 + 2 + 3 = 6.
Input & Output Format:
Input consists of one integer.
Output consists of a string. If it is a perfect number then display "Perfect Number" or else display "Not a Perfect Number".
Sample Input:
6
Sample Output:
Perfect Number


### CODE FOR THE PROBLEM ###

a=int(input())
b=0
for i in range(1,a):
    if(a%i==0):
        b+=i
if b==a:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
        


