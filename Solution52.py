### PROBLEM ###

Delete the Element
Requested files: Delete.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a C program to delete the element from the given location in an array:
Input & Output Format:
Input consists of two integer and one array.
First Input consists of size of an array.
Second give the array elements based on their size.
Third input consists of the position where we need to delete it.
Output consists of an array after deletion.
Sample Input:
5
1
2
3
4
5
4
Sample Output:
1
2
3
5

### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
c=int(input())
for i in range(a):
    if(b[i]!=c):
        print(b[i])
