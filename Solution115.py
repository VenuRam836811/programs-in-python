### PROBLEM ###


You must output the word in a list of correct words that is a scrambled version of an incorrectly written input, regardless of the case.
Input
Line 1: An integer N for the number of words in the dictionary.
Line 2: SCR, the scrambled word.
Next N lines: A list ACC of accepted words.
Output
Line 1: The word in the dictionary the misspelled word is a scrambled version of.
Constraints
2 ≤ N ≤ 100
2 ≤ len(SCR) ≤ 20
All dictionary words include only letters.
The dictionary does not contain anagrams.
Example
Input
3
Bannaa
Five
Banana
Tree
Output
Banana


### CODE FOR THE PROBLEM ###



import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
scr = input()
a=0
max=0
for i in range(n):
    acc = input()
    a=0
    for j in range(len(acc)):
        if acc[j] in scr:
            a+=1
            if a>max:
                str=acc
                max=a
print(str)

