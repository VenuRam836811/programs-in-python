### PROBLEM ###

Pattern II
Requested files: Pattern2.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a Python program to print the given pattern from user-defined values(dynamic values)

Sample Input 1:
5
Sample Output 1:
11111
22222
33333
44444
55555

Sample Input 2:
7
Sample Output 2:
1111111
2222222
3333333
4444444
5555555
6666666
7777777

### CODE FOR THE PROBLEM ###

a=int(input())
for i in range(1,a+1):
    for j in range(a):
        print(i,end='')
    print()
