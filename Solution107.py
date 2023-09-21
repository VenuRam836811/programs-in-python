### PROBLEM ###

You have to find out if the numbers GLaDOS gives you, mean that there is a cake or not.
You are given three numbers, n, t and c, n being the amount of cakes.
While t stands for how delicious the cake is, c stands for the amount of candles on it.

There is no cake with more that 14 candles on it. (It's just not possible in this universe)
And there is no cake being more delicious than grandma's cake (t=101)
And if a cake has negative/zero taste (t) OR candles (c), it simply is not a cake.
Input
First line: You are given an integer n.
Next n lines: You are given two space-separated integers t and c.
Output
n lines: With the appropriate text That's a cake! or GLaDOS you filthy liar!, second meaning that there is no cake.
Constraints
0 < n ≤ 100
-1000≤ t ≤ 1000
-1000 ≤ c ≤ 1000
Example
Input
1
5 2
Output
That's a cake!


### CODE FOR THE PROBLEM ###

import math
n=int(input())
for i in range(n):
    t,c=[int(j) for j in input().split()]
    if t>101 or c>14 or c<=0:
        print("GLaDOS you filthy liar!")
    else:
        print("That's a cake!")
