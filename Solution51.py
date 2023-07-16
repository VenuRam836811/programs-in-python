### PROBLEM ###

Sort the array in ascending order
Requested files: Sort.py (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to sort the given list in ascending order:
Input & Output Format:
Input consists of 1 integer and 1 array
First input consists of size of an array.
Second inputs consists of an elements depends upon their size.
Output consists of an array in ascending order.
Sample Input:
5
54
68
25
14
74
Sample Output:
14
25
54
68
74

### CODE FOR THE PROGRAM ###

a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
b.sort()
print(b)
