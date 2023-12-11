### PROBLEM ###


You are a Master Chief Spartan John-117 fellow fan, but you're also a Spartan.
As Spartan, you have a lot of different tasks and today, your Major gave you the order to decode a new kind of code that Floods used to counter your hero.

You have to decrypt intercepted messages from Floods and prevent any damage.
As regular decrypter you know some tips :

The Floods encode a message by converting each character in it to its ASCII code in hexadecimal. Then, if the length of the message is odd, the list of hexadecimals is reversed; otherwise, the list remains unchanged.
Input
Line 1 : n message length
n Next lines : an hexadecimal string chain
Output
Line 1 : The target's Flood
Constraints
0 < n <= 50
Example
Input
8
4a
6f
68
6e
2d
31
31
37
Output
John-117



### CODE FOR THE PROBLEM ###


n=int(input())
s=""
for i in range(n):
    l=input()
    a=int(l,16)
    s+=chr(a)
if n%2==0:
    print(s)
else:
    print(s[::-1])
