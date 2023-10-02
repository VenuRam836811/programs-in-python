### PROBLEM ###


You are given a string. You need to print no and count of either COWS or MILK if COWS and MILK (as a word) appear same number of times in string, otherwise print counts of COWS and MILK respectively.

The string contains words with uppercase letters only and spaces separate each word.

Note: COW, MOSCOW, MOSCOWS etc are all different from COWS and not consider as a COWS.
Input
A string s
Output
Print no and count of either COWS or MILK if COWS and MILK (as a word) appear same number of times in string, otherwise print counts of COWS and MILK respectively.
Constraints
0 < length of s < 256
Example
Input
COWS AND MILK
Output
no 1


  ### CODE FOR THE PROBLEM ###


s=input().split(" ")
a=b=0
for i in s:
    if i=="COWS":
        a+=1
    if i=='MILK':
        b+=1
if a==b:
    print('no',a)
else:
    print(a,b)
