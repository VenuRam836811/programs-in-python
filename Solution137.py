### PROBLEM ###


Extra characters are scattered in the sentences, among them: ' ? ! / , . : ) %
Your task is to count how many such characters are in a sentence.

! Space is not extra character !
Input
One sentence
Output
One number - quantity of extra characters
Constraints
3 <= lengh of sentence <= 100
Example
Input
Where's your motivation?
Output
2


### CODE FOR THE PROBLEM ###



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s=input()
a=0
for i in s:
    if i.isalpha() or i==" ":
        a+=1
print(len(s)-a)
