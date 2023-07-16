### PROBLEM ###

Sum of array elements
Requested files: Sumarray.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to find the sum of elements in an array.
Sample Input:
3
1
2
3
Sample Output:
6

### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
c=d=0
for i in range(a):
    b.append(int(input()))
for i in range(a):
    c+=b[i]
print(c)
