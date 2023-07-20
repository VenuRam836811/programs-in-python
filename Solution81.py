### PROBLEM ###

Given a string s, you must convert it to aLtErNaTiNg CaSe, and then output only the alphabetic characters out it.
Input
A string s
Output
s but in aLtErNaTiNg CaSe
Constraints
0 <= len(s) <= 1500
Characters can only be a-z A-Z 0-9
Example
Input
sdg9ad71gg
Output
sDgaDgG

### CODE FOR THE PROBLEM ###

a=input()
for i in a:
    b=a.index(i)
    if i.isalpha():
        if(b%2==0):
            print(i.lower(),end='')
        elif b%2==1:
            print(i.upper(),end='')
            
