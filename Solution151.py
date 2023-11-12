### PROBLEM ###


  Change K in such way so that the word is inside out, meaning the first half and second half are reversed by themselves. If the length of the string is odd, leave the center character in the center, so that applying your code on your output should turn it back into K.

Examples:
duck -> udkc
crazy -> rcayz
codingame-> idocnemag
Input
The word K containing alphabetic lowercase characters only.
Output
The inside out version of K
Constraints
4 ≤ Length of K ≤ 100
Example
Input
duck
Output
udkc



  ### CODE FOR THE PROBLEM ###


  import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

k = input()
a=len(k)//2
b=0
if(len(k)%2==0):
    for i in range(2):
        print(k[b:a][::-1],end="")
        b=a
        a=a+a
else:
    for i in range(2):
        print(k[b:a][::-1],end="")
        if i==0:
            print(k[a],end="")
        b=a+1
        a+=a+1

