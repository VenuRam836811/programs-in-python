### PROBLEM ###


In order to pass the United States Registered Professional Reporter test, you must be able to type at a minimum of 180 words per minute with very high, at least 90%, degree of accuracy.
The degree of accuracy can be calculated number of matching characters (spaces and punctuation included, case insensitive for alphabetic characters) divided by the total length of the string.
Your task as the exam corrector is to assess whether each submission has a sufficient degree of accuracy to "pass" or "fail" given the criteria.
Input
Line 1: The key phrase each submission must compare to.
Line 2: The number of submissions.
Next n lines: Each submission
Output
The result of each submission in the form of "pass" or "fail".
Constraints
*Length of key > 0
*Length of a submission is always the same length as key
*Number of submissions < 10
Example
Input
We will now begin with opening statements
1
We will now begin with opening statements
Output
pass


### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

key = input()
key=key.lower()
n = int(input())
a=0
for i in range(n):
    s= input()
    s=s.lower()
    b=len(s)
    a=0
    for m in range(len(s)):
        if(s[m]==key[m]):
            a+=1
    if((a/b)*100>=90):
        print("pass")
    else:
        print("fail")


