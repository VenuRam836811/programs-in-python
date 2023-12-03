### PROBLEM ###


Percent error is the difference between estimated value and the actual value in comparison to the actual value and is expressed as a percentage. In other words, the percent error is the relative error multiplied by 100.

Using the formula : Percent Error = |(Estimated Value - Actual Value) / Actual Value| * 100
Input
Line 1: An integer x for Estimated Value
Line 2: An integer y for Actual Value
Output
Line 1: The percentage rounded to 2 decimal places.
Constraints
Example
Input
1
2
Output
50.00%


### CODE FOR THE PROBLEM ###


import sys
import math
x = int(input())
y = int(input())
a=abs((x-y)/y)*100
print("{:.2f}%".format(a))
