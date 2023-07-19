### PROBLEM ###

The program:
Convert a string code of concatenated ASCII code numbers to the corresponding string of ASCII characters.

INPUT:
String of decimal numbers. Each number is 3 digits long and padded with zeroes.

OUTPUT:
The corresponding ASCII string.
If the input length is not a multiple of 3, then you should output the string ERROR.

CONSTRAINTS:
0 < Length of code ≤ 500
32 ≤ ASCII code ≤ 255

EXAMPLE:
Input
067111100105110103
Output
Coding


### CODE FOR THE PROBLEM ###

a=input()
b=len(a)//3
d=0
sum=0
if len(a)%3==0:
    for i in range(b):
        c=a[d:d+3]
        for j in c:
            e=int(j)
            sum=sum*10+e
        print(chr(sum),end='')
        sum=0
        d=d+3
else:
    print("ERROR")
