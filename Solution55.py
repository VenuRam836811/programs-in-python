### PROBLEM ###

Maximum Values
Requested files: Max.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to find the maximum element in an array:
Sample Input:
5
1
2
33
4
5
Sample Output:
33

### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
c=0
for i in range(a):
    b.append(int(input()))
for i in range(a):
    if(b[i]>c):
        c=b[i]
print(c)
