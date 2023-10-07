### PROBLEM ###


There are N pillars near the road. The distance D between the pillars is the same and the width W of each pillar is the same. Calculate the distance between the edges of the two outmost pillars (without the width of the first and last pillar).
Input
Line 1: Number N of pillars
Line 2: Distance D between pillars
Line 3: Width W of each pillar
Output
Line 1 : The total distance between the edges of the two outmost pillars
Constraints
2 ≤ N ≤ 100
1 ≤ D ≤ 100
1 ≤ W ≤ 100
Example
Input
2
1
1
Output
1



#### CODE FOR THE PROBLEM ###


a=int(input())
b=int(input())
c=int(input())
print((b*(a-1))+c*(a-2))
