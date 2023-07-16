### PROBLEM ###

Count Odd or Even
Requested files: Count.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to count the number of even and odd elements in an array:
Sample Input:
3
1
2
3
Sample Output:
Odd: 2
Even: 1

### CODE FOR THE problem ###

a=int(input())
b=[]
c=d=0
for i in range(a):
    b.append(int(input()))
for i in range(a):
    if b[i]%2==0:
        c=c+1
    else:
        d=d+1
print("Odd: {}".format(d))
print("Even: {}".format(c))
