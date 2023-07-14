### PROBLEM ###

Friendly Pair
Requested files: Friendly.java (Download)
Maximum number of files: 5
Type of work: Individual work
 Program to find if the given numbers are Friendly pair or not (Amicable or not) is discussed here. Friendly Pair are two or more numbers with a common abundance.
Input & Output format: 
Input consists of 2 integers.
The first integer corresponds to number 1 and the second integer corresponds to number 2.
If it is a Friendly Pair display Friendly Pair or displays Not Friendly Pair.
For example,6 and 28 are Friendly Pair.
(Sum of divisors of 6)/6 = (Sum of divisors of 28)/28.
Sample Input:
6
28
Sample Output:
Friendly Pair


### CODE FOR THE PROBLEM ###


def pair1(a,c):
    a1=0
    for i in range(1,a+1):
        if a%i==0:
            a1+=i
    c=a1/a
    return c
def pair2(b,d):
    a2=0
    for i in range(1,b+1):
        if b%i==0:
            a2+=i
    d=a2/b
    return d

    
a=int(input())
b=int(input())
c,d=0,0
pair1(a,c)
pair2(b,d)
if c==d:
    print("Friendly Pair")
else:
    print("Not Friendly Pair")

