### PROBLEM ###


In this Clash of Code, your task is to write a function that processes a camelCase sentence.
Your goal is to convert the camelCase sentence into a sentence in which each word is :
- separated by a space,
- only the first letter of the entire sentence is capitalized.
Input
A : a string in a camelCase format
Output
Line 1 : The string in a "sentence case" format
Constraints
A contains only uppercase and lowercase letters.
The maximum length of A is 50 characters.
Example
Input
firstTestOfTheClash
Output
First test of the clash


  ### CODE FOR THE PROBLEM ###



a=input()
for i in range(len(a)):
    if i==0:
        print(a[i].upper(),end='')
    else:
        if a[i].islower():
            print(a[i],end='')
        elif a[i].isupper():
            print(" ",end='')
            print(a[i].lower(),end='')

