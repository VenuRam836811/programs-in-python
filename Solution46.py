### PROBLEM ###

Sum of Numbers in a range
Requested files: Sumofnum.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to find the sum of numbers in a given range is discussed here. Given the starting and ending interval, the sum of all the numbers in that range will be displayed as output.
For example,
Input: 1 10
Output: 55
Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
Input & Output Format:
Input consists of two integers.
First input consists of the start value.
Second input consists of the end value.
Output consists of the sum of range.
Sample Input 1:
1
10
Sample Output 1:
55

### CODE FOR A PROBLEM ###

def sum(a,b):
    ra=0
    for i in range(a,b+1):
        ra+=i
    return ra
a=int(input())
b=int(input())
print(sum(a,b))

