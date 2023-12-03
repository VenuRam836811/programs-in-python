### PROBLEM ###


Your task is to output a cone of n rows. The first row is made up of a space characters and a symbol. In each successive row, both the number of space characters and the number of symbol characters increase by 1.
Input
Line 1 : An integer n for the height of the cone
Line 2 : An integer a for the number of space characters in the first row of the cone
Line 3 : A string symbol
Output
The cone
Constraints
n > 0
a ≥ 0
Example
Input
10
5
*
Output
      *
       **
        ***
         ****
          *****
           ******
            *******
             ********
              *********
               **********


  ### CODE FOR THE PROBLEM ###


import sys
import math
n = int(input())
a = int(input())
s = input()
for i in range(0,n):
    print(" "*(a+1+i)+s*(i+1))
