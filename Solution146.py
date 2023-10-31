### PROBLEM ###


Given a board with w x h squares, what's the maximum amount of rooks that could to be placed such that only 1 pair of rooks are attacking each other?

A rook attacks in straight lines. If another rook was on a rook's left, right, up or down, that rook is being attacked.
Input
2 integers w, h
Output
The maximum amount of rooks
Constraints
1 <= w, h <= 50
Example
Input
8 8
Output
8


### CODE FOR THE PROBLEM ####


w,h =[int(i) for i in input().split()]
if w==h:
    print(h)
else:
    print(((w*h)//max(w,h))+1)
