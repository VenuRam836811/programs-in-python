## PROBLEM ###


You must output the possible pair of numbers as a solution for given sudoku group, considering filled numbers, result group sum and sudoku rule.

Sudoku rule states that only 1-9 digits can be used without repetition.
Result group sum is a rule of Killer sudoku, where few cells are combined into a group defined by sum of numbers (pair in given case).
Filled numbers is a limitation for numbers, which were already used to define sudoku section and can not be used in solution.
Input
Line 1: An integer N for the number of filled numbers
Line 2: N space separated integers, describing filled numbers
Line 3: An integer S for the expected result group sum
Output
Line 1: Space separated integers in ascending order, which sum fits sudoku group solution
Constraints
0<N<10 count of filled numbers
N unique numbers in range 1-9, provided in ascending order
3<=S<=17 expected sum of resulting unique pair
Only one pair of numbers is valid for the solution
Example
Input
1
7
3
Output
1 2



### CODE FOR THE PROBLEM ###



n=int(input())
l=[]
for i in input().split():
    f=int(i)
    l.append(f)
s=int(input())
for i in range(1,10):
    for j in range(i+1,10):
        if i and j not in l:
            if s==i+j:
               a=i
               b=j
print(a,b)

