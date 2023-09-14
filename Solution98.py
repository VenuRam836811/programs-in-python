### PROBLEM ###


You are part of the decision-making quorum of a hidden country.
This quorum is made up of 10 members and you are the 10th.
Quorum is invoked to make a Yes/No decision.
For the quorum decision to be valid, at least one of the members must disagree with the others. as you are the 10th, your decision may therefore be constrained. In this case, you will add an exclamation point at the end of your decision (example: if there are 9 Yes before you, you must say No!).
In the event that your decision is not constrained, you will side with the opinion of the majority (example: if there are 7 Yes and 2 No before you, you must say Yes).
Input
Line 1 : A character string votes containing the previous votes separated by a space
Output
Line 1 : your_vote that represents your decision Yes, No, Yes! or No!
Constraints
Example
Input
Yes Yes Yes Yes Yes Yes Yes Yes Yes
Output
No!
                                                                                                    

### CODE FOR THE PROBLEM ###
                                                                                                    
import sys
import math
votes = input()
a=b=0
s=votes.split(" ")
for i in s:
    if i=='Yes':
        a+=1
    elif i=='No':
        b+=1
c=len(s)
if(c==a):
    print("No!")
elif c==b:
    print("Yes!")
elif a<b:
    print("No")
else:
    print("Yes") 
