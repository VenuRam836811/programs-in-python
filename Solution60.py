### PROBLEM ###

Addition of two arrays
Requested files: Add.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to add two arrays:
Input & Output Format:
First Input consists of size of an array for two arrays
Second Input consists of first array elements.
Third Input consists of second array elements.
Output consists of an array
Sample Input:
3
1
2
3
4
5
6
Sample Output:
5 7 9

### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
c=[]
for i in range(a):
    c.append(int(input()))
d=[]
for i in range(a):
    d.append(b[i]+c[i])
print(d)
    
