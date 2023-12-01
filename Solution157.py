### PROBLEM ###


Over the centuries a language evolves, and not only do words appear or disappear, but some letters become more used or on the contrary less used.

In order to be able to quickly analyze many texts, we want to develop a program that calculates how many times a given letter is present in a text.
Input
Line 1: A character C that will be searched for
Line 2: An integer N
Next N lines: a string with length len
Output
the number of times that C appears in the text
Constraints
0 ≤ len ≤ 1000
Example
Input
E
2
JE VOUS REMECTZ A LA GRANDE CHRONICQUE PANTAGRUELINE 
RECONGNOISTRE LA GENEALOGIE ET ANTIQUITE DONT NOUS EST VENU GARGANTUA
Output
16


### CODE FOR THE PROBLEM ###


c = input()
m=c[0]
a=0
n = int(input())
for i in range(n):
    ligne = input()
    for j in ligne:
        if j==m:
            a+=1
print(a)
