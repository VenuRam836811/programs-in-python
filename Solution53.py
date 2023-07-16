### PROBLEM ###

Printing the Values
Requested files: Print.java (Download)
Maximum number of files: 5
Type of work: Individual work
Adam was learning about storage structure with the help of Roz. Roz's first task was to make Adam understand the concept of array by asking Adam to create an array dynamically and get the inputs into the array and print the array. As Adam had confusion she has approached you for help.
Help Adam by writing a program to create an array , get inputs and print the inputs.
Sample Input:
3
1
2
3
Sample Output:
1
2
3

### CODE FOR THE PROGRAM ###

a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
for i in range(a):
    print(b[i])
