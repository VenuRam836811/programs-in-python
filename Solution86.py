### PROBLEM ###

Shadoks are simple creature. They like pumping whole day.
1 pump action is completed once the 4 "Ga Bu Zo Meu" instructions has been performed in this order.
Listen to s the Shadoks speech and return PumpCount the number of completed pump actions performed.
Additional instructions will not affect the count.
As an example:
Ga Ga Bu Meu Zo Meu
Counts as 1.
Input
Line 1: s String of Shadok instructions separated by spaces.
Output
Ligne 1: n the number of completed pump actions.
Constraints
0 ≤ PumpCount ≤ 100
0 ≤ s ≤ 1000
Example
Input
Ga Bu Zo Meu
Output
1

### CODE FOR THE PROBLEM ###
  
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a=s.split(" ")
count=0
for i in a:
    if i=="Meu":
        count+=1
    if i=="GGGGa":
        count-=1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(count)
