### PROBLEM ###

Search the element
Requested files: Search.python (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to search an element whether it is present in the array or not:
Input & Output Format:
Input consists of 2 integer and 1 array.
First input consists of a size of an array.
second give the array elements as input.
Third input consists of the element that you want to search.
Output consists of a string. 
If the element is present print the value and display " is present in the list" or else 
"is not present in the list"
Sample Input:
3
10
15 
5
10
Sample Output:
10 is present in the array

### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
d=0
for i in range(a):
    b.append(int(input()))
c=int(input())
for i in range(a):
    if(b[i]==c):
        print("{} is present in the list".format(c))
        break
    else:
        d+=1
if d==a:
    print("{} is not present in the list".format(c))
