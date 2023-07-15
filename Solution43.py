### PROBLEM ###

Prime Number
Requested files: Prime.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to find whether the given number is Prime number or Not.
Input & Output Format:
Input consists of one integer.
Output consists of a string.
If it is prime then display "Prime Number" or if it is not prime then display "Not a Prime"
Sample Input:
2
Sample Output:
Prime Number



### CODE FOR THE PROBLEM ###

a=int(input())
c=0
if a==0 or a==1:
    print("Prime Number")
else:
    for i in range(2,a+1):
        if a%i==0:
            c+=1
    if c==1:
        print("Prime Number")
    else:
        print("not a Prime Number")
