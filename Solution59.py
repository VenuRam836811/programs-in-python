### PROBLEM ###

Same or not
Requested files: Same.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to find whether two arrays are same or not. Two arrays are said to be same if the sum of both the arrays are same and size of arrays are same:
INPUT FORMAT:
Input consists of 1 integers and 2 arrays.
Integers correspond to the size of arrays.
If two arrays are same, display "Same" else display "Not Same"
Sample Input:
3
3
1
2
3
1
2
3
Sample Output:
Same


### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
c=[]
d=0
for i in range(a):
    b.append(int(input()))
for i in range(a):
    c.append(int(input()))
for i in range(a):
    if(b[i]==c[i]):
        d+=1
if d==a:
    print("Same")
else:
    print("Not Same")
