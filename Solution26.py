### PROBLEM ###

Requested files: Garden.java (Download)
Maximum number of files: 5
Type of work: Individual work
Dora is interested so much in gardening and she plants more trees in her garden. She plants trees in a rectangular fashion with the order of rows and columns and numbered the trees in row-wise order. She planted the mango tree only in a 1st row, 1st column and last column. So given the tree number, your task is to find whether the given tree is a mango tree or not? Write a program to check whether the given number is a mango tree or not. 

Input format: 

Input consists of 3 integers 

The first input denotes the number of rows 

The second input denotes the number of columns 

The third input denotes the tree number 

Output format:

 If the given number is a mango tree, print "Yes". 

Otherwise, print "No" 

Refer the sample output for formatting

Sample Input:

5

5

11  

Sample Output:

Yes

### CODE FOR THE PROGRAM ###


a=int(input())
b=int(input())
c=int(input())
if(c>=1 and c<=a or c%a==0 or c%b==1 ):
    print("Yes")
else:
    print("No")
        
