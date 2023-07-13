### PROBLEM ###


Vowel Or Consonants
Requested files: Vowcons.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to check whether the given character is vowel or consonant or Not an alphabet.

Input format: 

The input consist of a character 

Output format: 

The output consists of a below-given string “Vowel” / “Consonant” / “Not an alphabet”

Sample Input: 

a 

Sample Output: 

Vowel



  ### CODE FOR THE PROBLEM ###


c=input()
if c>='a' and c<='z':
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
