### PROBLEM ###


Lab Allocation
Requested files: Lab.java (Download)
Maximum number of files: 5
Type of work: Individual work
There are 3 labs in the CSE department (L1, L2 and L3) with a seating capacity of x, y and z. find the lab which has the minimal seating capacity. 
Input and Output Format:
Assume that x, y and z are always distinct.
Refer sample input and output. 
Note:
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
Enter x
30
Enter y
40
Enter z
20
L3 has the minimal seating capacity

### CODE FOR PROBLEM ###


x=int(input("Enter x\n"))
y=int(input("Enter y\n"))
z=int(input("Enter z\n"))
if x<y and x<z:
    print("L1 has the minimal seating capacity")
elif y<x and y<z:
    print("L3 has the minimal seating capacity")
else:
    print("L3 has the minimal seating capacity")
    
