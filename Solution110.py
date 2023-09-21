### PROBLEM ###

Users of Filmweb can rate a movie on a 1 to 10 star rating scale. Each of the star rating corresponds to a description. You are given N lines of strings (ratings) of length 10. Each string starts with a number of * representing the number of stars given by a user, and - fills out the rest of the spots. All possibilities with their descriptions are given below:

1/10:     *---------     Mistake
2/10:     **--------     Very bad
3/10:     ***-------     Bad
4/10:     ****------     So so
5/10:     *****-----     Average
6/10:     ******----     Quite good
7/10:     *******---     Good
8/10:     ********--     Very good
9/10:     *********-     Sensational
10/10:    **********     Masterpiece!

Your goal is to calculate the average rating of the movie, round it to the closest integer and output the description of the rounded average.
Input
Line 1: An integer N for the number of people rating the movie.
Next N lines: A string rating representing the rating given by each person.
Output
Line 1: The string description for the movie according to its average rating.
Constraints
0 < N <= 100
rating.length = 10
Example
Input
4
*******---
*****-----
*******---
*****-----
Output
Quite good


### CODE FOR THE PROBLEM ###


import sys
import math
n = int(input())
a=0
for i in range(n):
    rating = input()
    for j in rating:
        if j=='*':
            a+=1
b=int(round(a/n))
if b==1:
    print("Mistake")
elif b==2:
    print("Very bad")
elif b==3:
    print("Bad")
elif b==4:
    print("So so")
elif b==5:
    print("Avarage")
elif b==6:
    print("Quite good")
elif b==7:
    print("Good")
elif b==8:
    print("Very good")
elif b==9:
    print("Sensational")
else:
    print("Masterpiece!")

