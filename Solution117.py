### PROBLEM ###


Given a blank space of a certain length (lengthOfBlanks) and a fullQuote, print the words of that quote that will fit in that blank space.
We'll call this partialQuote but please note that sometimes the entire fullQuote will fit.

Also, you will print some meta-data about this partialQuote: the number of words and the number of characters

Notes:
‣ Start with the first word and go in order. In other words, start at the beginning and put as much of the quote that will fit (whole words only)
‣ Padding on either side is NOT needed
‣ For simplicity anything next to a word is considered part of the word. For example software, including the comma is a "word"
‣ A hyphenated-word counts as a single word; for example logic-based counts as one word


~ ~ ~ ~ ~ ~ ~ ~
Source of quotes:
https://techvify-software.com/35-best-coding-programming-quotes/
Input
Line 1: An integer, lengthOfBlanks
Line 2: A string, fullQuote
Output
Line 1: partialQuote
Line 2: The number of words in partialQuote followed by words
Line 3: The number of characters (including spaces) in partialQuote followed by characters long
Constraints
lengthOfBlanks ≥ 3

partialQuote always consists of more than one word.

fullQuote never starts with a space character.
Example
Input
24
Programming is learned by writing programs.
Output
Programming is learned
3 words
22 characters long


### CODE FOR THE PROBLEM ###


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l=int(input())
f=input().split(" ")
a=0
b=1
str=""
for i in f:
    a+=len(i)
    if(a<=l):
        str=str+i+" "
    if a>l:
        break
    a+=1
for i in range(len(str)-1):
    print(str[i],end="")
    if str[i]==' ':
        b+=1
print()
print(b,"words")
print(len(str)-1,"characters long")


