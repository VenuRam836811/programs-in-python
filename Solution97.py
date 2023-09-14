### PROBLEM ###

The program:
You must output the characters that are identical at the begin and the end of the string when reading respectively from left to right and right to left.
An uppercase letter is equal to its lowercase variant.
INPUT:
A string S.
OUTPUT:
A string corresponding to the characters present at the begin and the end of the string S. Print Nothing if the first letter and the last letter are different.
CONSTRAINTS:
Length of S is lower than 99 characters. It can contain spaces and punctuation marks.
EXAMPLE:
Input
abcdefgdcba
Output
abcd

### CODE FOR THE PROBLEM ###

s=input()
s=s.lower()
a=0
if s[0]!=s[len(s)-1]:
    print("Nothing")
for i in range(len(s)):
    if i<len(s)/2:
        if(s[i]==s[len(s)-1-i]):
            print(s[i],end='')
        else:
            break
        
        
 
