### PROBLEM ###


The word palindrome is the same word if you read it from right to left or from left to right.
Check if the given string word is a palindrome or no
Please ignore case of letters : e.g Radar = radaR is a palindrome
Our algorithm must return the result palindrome , not palindrome or invalid
The word is considered invalid when it contains a number
Input
Line 1: word is an input of type string.
Output
Line 1: Result representing if word is a palindrome ( palindrome or not palindrome or invalid )
Constraints
2 < word.length < 100
Example
Input
ada
Output
palindrome



### CODE FOR THE PROBLEM ###


word = input().lower()
word1=word[::-1]
a=0
for i in word:
    if i.isdigit():
        a=1
if a==1:
    print("invalid")
elif word==word1:
    print("palindrome")
else:
    print("not palindrome")
