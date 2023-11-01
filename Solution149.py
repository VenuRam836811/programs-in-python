### PROBLEM ###


Given a circuit either series or parallel, find the total resistant R.
If the circuit is series, R = r1 + r2 + r3 + ... + rn
If the circuit is parallel, 1/R = 1/r1 + 1/r2 + 1/r3 + ... + 1/rn
Input
Line 1: Either series or parallel : the circuit type.
Line 2: An integer n for the number of resistors.
Line 3: n space-separated integers r1, r2, r3, ..., rn.
Output
An integer R for the total resistant.
In case of parallel circuit, output R rounded to 2 decimal places.
Constraints
1 <= n <= 100
1 <= r <= 1000
Example
Input
series
5
1 2 3 4 5
Output
15



### CODE FOR THE PROBLEM ###


s= input()
n=int(input())
m=a=0
for i in input().split():
    r = int(i)
    if s=="series":
        m+=r
    else:
        a=1
        m+=1/r
if a==0:
    print(m)
else:
    print(f"{1/m:.2f}")


