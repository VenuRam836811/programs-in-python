### PROGRAM ###

Remove duplicates of an array
Requested files: Remove.python (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to remove the duplicate elements from an array:
INPUT FORMAT:
Input consists of 1 integer and 1 array.
The first integer corresponds to the size of the array.
The next integers correspond to the elements in the array.
OUTPUT FORMAT:
The output consists of an array with no duplicate elements.
Sample Input:
5
1
2
3
4
4
Sample Output:
1 2 3 4 

### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
d=0
for i in range(a):
    b.append(int(input()))
c=[*set(b)]
print(c)
