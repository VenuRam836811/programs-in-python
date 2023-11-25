### PROBLEM ###


In European tunnels, emergency exits need to be within 500 meters of each other.

You are an inspector following European regulations, inspecting plans for an upcoming tunnel. You have listed all of the planned emergency exits, sorted by their distance from one of the entrances, and have verified that the first and last exits are close enough to the entrances.

However, your supervisor tells you that two exits are too far from each other!

You need to find these two exits, and determine the distance separating them.
Input
First line: An integer N for the number of emergency exits.
Second line: N space-separated integers representing the distance of every emergecy exit to the entrance.
Output
First line: The distance between the two emergency exits that are too far apart.
Constraints
2 <= N <= 100
Example
Input
3
200 600 1700
Output
1100



### CODE FOR THE PROBLEM ###


import sys
import math
n = int(input())
max=0
for i in input().split():
    distance = int(i)
    if distance-max>500:
        print(distance-max)
        break
    else:
        max=distance

