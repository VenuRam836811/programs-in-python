### PROBLEM ###

Gregory was born on February 29. He therefore celebrates his birthday on the 29th every 4 years, when it's a leap year. In other years, he celebrates it on the 28th.
You are given Gregory's age age, his year of birth year, and you must return the number of times he celebrated his birthday on the 29th.
The year of birth doesn't count
Hint: to be a leap year, the year must be:
-Divisible by 4 and not divisible by 100
-Divisible by 4, by 100 and by 400
Input
Line 1: An integer for Gregory's age age
Line 2: An integer for his year of birth year
Output
The number of times he celebrates his birthday on the 29th
Constraints
0 ≤ age ≤ 120
-47 ≤ year ≤ 2050
Example
Input
12
2000
Output
3

### CODE FOR THE PROBELM ###

a=int(input())
y=int(input())
b=0
for i in range(a):
    y+=i
    if y%4==0:
        b+=1
print(b)
