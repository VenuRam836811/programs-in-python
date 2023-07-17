### PROBLEM ###

Count the distinct elements
Requested files: Countdistinct.python (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to count the distinct elements in an array:
Input & Output Format:
Input consists of 1 integer and 1 array.
First input consists of size of an array.
Second inputs corresponds to the array elements.
Output consists of one integer and corresponds to the count of the distinct elements.
Sample Input:
6
2
6
6
4
5
5
Sample Output:
4

### CODE FOR THE PROBLEM ###

a=int(input())
a1=list(map(int,input().split()))
a2=[*set(a1)]
print(len(a2))
