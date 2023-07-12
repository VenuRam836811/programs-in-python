### PROBLEM ###

Sum and Difference
Requested files: SumDiff.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to get 2 numbers from the user and calculate their sum and difference using '+' and '-' operators respectively. Print the corresponding sum and difference of the numbers as output in the console.

 Input format:

First input: an integer 

Second input: an integer 

Output format:

First output will be the sum of two integers

Second output will be the difference of two integers

Sample Input:

55

34

Sample Output:

89

21

### CODE FOR THE PROBLEM ###


def sum(a,b):
    print(a+b)
def diff(a,b):
    print(a-b)
a=int(input())
b=int(input())
sum(a,b)
diff(a,b)
