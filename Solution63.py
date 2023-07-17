### PROBLEM ###

Reverse an Array
Requested files: Reverse.py (Download)
Maximum number of files: 5
Type of work: Individual work
Write a python program to reverse an array:
Input & Output Format:
Input consists of 1 integer and 1 array.
First input consists of the size of an array.
Second inputs consists of array elements based on their array size.
Sample Input:
3
1
2
3
Sample Output:
3
2
1

  ### CODE FOR THE PROGRAM ###

a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
b.reverse()
print(b)
