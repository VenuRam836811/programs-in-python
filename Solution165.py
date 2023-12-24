### PROBLEM ###


If you read the book or watched the movie "Fight Club" you know about Narrator and Tyler Durden. Even if didn't - don't worry, because this puzzle is easy to understand. When Narrator snaps his fingers, he stops talking and Tyler starts. When Tyler snaps his fingers, he stops talking and Narrator starts.
You are given a conversation between Narrator and Tyler, in which Narrator begins, and a snap is represented as *Snap*. You must find out who talks last.

Example: sentence *Snap* sentence
Here the last sentence is Tyler's.
Input
Line 1: A string CONVERSATION
Output
print Narrator if the last one was Narrator, Tyler if the last one was Tyler and If what you're given, has no snaps, it's not a conversation, but a monologue. In such cases, you must output None of them
Constraints
0 <= quantity of snaps <= 6
Example
Input
Whoa, wait, this is crazy. You want me to hit you? *Snap* That’s right.
Output
Tyler



### CODE FOR THE PROBLEM ###



import sys
import math


conversation = input()
count=conversation.count("*Snap*")
if count==1:
    print("Tyler")
elif count>1:
    print("Narrator")
else:
    print("None of them")


