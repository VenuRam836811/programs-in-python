### PROBLEM ###

Prime Numbers in a Range
Requested files: Range.java (Download)
Maximum number of files: 5
Type of work: Individual work
Program to find prime numbers in a given range is discussed here. A number is said to be prime if it is divisible by 1 and the number itself. Program to find prime numbers in a given range using loop
Input & Output Format:
Input consists of two integers. 
First integer corresponds to lower value.
Second integer corresponds to upper value.
Output consists of the prime numbers between the two intervals.
Sample Input: 
1
10
Sample Output:
2
3
5
7


### CODE FOR THE PROBLEM ###

a=int(input())
b=int(input())
n=[]
c=d=0
for i in range(a+1,b):
    if i==0 or i==1:
        #n.append(i)
        print(i)
    else:
        c=0
        for j in range(2,i+1):
            if i%j==0:
                c+=1
        if c==1:
            #n.append(i)
            print(i)
