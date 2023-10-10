### PROBLEM ###


This clash is about the physics formula: Force = Mass * Acceleration

Based on the inputs force, mass and accel output the zero value input as the product of the other two (eg:accel=2,mass=2, then force=4 ; accel=2,force=20, then mass=10).
Input
force: The net force of the object.
mass: Mass of the object.
accel: Acceleration of the object.
Output
The force if mass and accel are non-zero.
The mass if force and accel are non-zero.
The accel if force and mass are non-zero.
"Not enough information" if two are zero inputs.
"No information" if all three are zero inputs.

The output should be a float. The float should be up to 1 decimal place if the answer is a whole number, and up to 2 decimal places if not.
Constraints
force >= 0
mass >= 0
accel >= 0
Example
Input
0
0
0
Output
No information


  ### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

f= float(input())
m= float(input())
a= float(input())
if f==m==a==0:
    print("No information")
else:
    if f==0 and m!=0 and a!=0:
        print(m*a)
    elif m==0 and f!=0 and a!=0:
        print(f/a)
    elif a==0 and f!=0 and m!=0:
        print(f/m)
    elif f==m==0 or f==a==0:
        print("Not enough information")

