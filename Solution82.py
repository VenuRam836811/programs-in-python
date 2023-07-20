### PROBLEM ###

Everyone at school with a friend came up with their own personal cipher for secret messages. Now you need to receive the message and encrypt it with the classic ASCII cipher. Having received the string s, you will need to sum up the ASCII codes of the lowercase vowels (which are a, e, i, o, u and y), and multiply the sum by their total number of appearances to get the final answer to output.
Input
Line 1: String s - received message
Output
Integer: Final product of letters
Constraints
Example
Input
sunshiny
Output
1029

### CODE FOR THE PROBLEM ###

import sys
import math
sum=c=0
a=input()
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y':
        sum+=ord(i)
        c+=1
print(sum*c)
