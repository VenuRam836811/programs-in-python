### PROBLEM ###

Area Calculation
Requested files: Area.java (Download)
Maximum number of files: 5
Type of work: Individual work
Sheela has three things in her bag. She wants to compute the area of 3 things but 3 things are in different shapes. The three things are in square shape, rectangular shape, and circular shape respectively. Write a program to help Sheela to calculate the area of different shapes. 

Input format: 

First input: a side of a square in integer 

Second input: length of a rectangle in integer 

Third input: breadth of a rectangle in integer 

Fourth input: radius of a circle in float 

Output format: 

The first output should be the area of a square in integer 

The second output should be the area of a rectangle in integer 

The third output should be the area of a circle in float with 2 decimal places

Sample Input: 

5

5

4

2.0

Sample Output: 

25

20

12.56



### CODE FOR THE PROBLEM ###


a=int(input())
b=int(input())
c=int(input())
d=float(input())
print(a*a)
print(b*c)
e=3.14*d*d
print(f"{e:.2f}")
