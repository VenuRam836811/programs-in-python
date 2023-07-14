### PROBLEM ###

Palindrome of a number
Requested files: Palindrome.py (Download)
Maximum number of files: 5
Type of work: Individual work
Program to check whether the given number is a Palindrome or  Not a Palindrome is discussed here. Any number is said to be a palindrome if the original number and the reverse of the original number are the same.
For example, 1234321 is a palindrome.
Original number = 1234321
The reverse of the number = 1234321
Sample Input:
454
Sample Output:
Palindrome

### CODE FOR THE PROBLEM ###

a=int(input())
c=a
digit=0
while a>0:
    b=a%10
    digit=digit*10+b
    a=a//10
if digit==c:
    print("Palindrome")
else:
    print("not palindrome")


