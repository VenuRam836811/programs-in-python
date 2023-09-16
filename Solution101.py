### PROBLEM ###

Given a string S, you should calculate an integer R which is the result of summing all S's digits except the first one, and then multiplying the result with the first digit.
if S is not an integer print INVALID

NOTES:
- Be careful, the first number may be negative (starting with '-') !
- Strings starting with '0' are considered valid, example : '012' => 0

Example:
S(Input)=123
R(Output)=1*(2+3)=5
Input
String S
Output
The result R
if the input is not a number print INVALID
Constraints
-100000<R<100000
Example
Input
123
Output
5


### CODE FOR THE PROBLEM ###

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
sum=0
try:
    int(s)
except:
    print("INVALID")
for i in range(1,len(s)):
    sum+=int(s[i])
a=int(s[0])
print(a*sum)





