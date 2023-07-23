### PROBLEM ###

You need to find the Crazy Factorial of a given number n.

--> What exactly is a Crazy Factorial?

It means after computing the factorial of n, the result will be divided by Sum of the Digits in the number.

--> Example:

n = 5. 5! = 5 * 4 * 3 * 2 * 1 which is 120. 120 has 3 digits- 1,2,0 and 1+2+0=3, so you divide 120 by 3 = 40 the Crazy Factorial of 5.

Note: It can be shown that the Crazy Factorial is always an integer under the current given constaints.
Input
An Integer n
Output
Print the Crazy Factorial of n.
Constraints
0 < n <= 20
Example
Input
5
Output
40

### CODE FOR THE PROBLEM ###

a=int(input())
sum=1
for i in range(1,a+1):
    sum*=i
c=0
z=sum
while(sum!=0):
    b=sum%10
    c+=b
    sum=sum//10
print(int(z/c))
