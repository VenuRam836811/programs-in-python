### PROBLEM ###


The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
123456789
12345
23456
34567
45678
56789
02 Test 2
Input
Expected output
>CodinGame<
>Codin
CodinG
odinGa
dinGam
inGame
nGame<
03 Test 3
Input
Expected output
s : : : : : : : : : : : : : : / : : : : : : : : : : : : : : e
s : : : : : : : : : : : : : : /
 : : : : : : : : : : : : : : / 
: : : : : : : : : : : : : : / :
 : : : : : : : : : : : : : / : 
: : : : : : : : : : : : : / : :
 : : : : : : : : : : : : / : : 
: : : : : : : : : : : : / : : :
 : : : : : : : : : : : / : : : 
: : : : : : : : : : : / : : : :
 : : : : : : : : : : / : : : : 
: : : : : : : : : : / : : : : :
 : : : : : : : : : / : : : : : 
: : : : : : : : : / : : : : : :
 : : : : : : : : / : : : : : : 
: : : : : : : : / : : : : : : :
 : : : : : : : / : : : : : : : 
: : : : : : : / : : : : : : : :
 : : : : : : / : : : : : : : : 
: : : : : : / : : : : : : : : :
 : : : : : / : : : : : : : : : 
: : : : : / : : : : : : : : : :
 : : : : / : : : : : : : : : : 
: : : : / : : : : : : : : : : :
 : : : / : : : : : : : : : : : 
: : : / : : : : : : : : : : : :
 : : / : : : : : : : : : : : : 
: : / : : : : : : : : : : : : :
 : / : : : : : : : : : : : : : 
: / : : : : : : : : : : : : : :
 / : : : : : : : : : : : : : : 
/ : : : : : : : : : : : : : : e
04 Test 4
Input
Expected output
Programming is logic-based creativity
Programming is logi
rogramming is logic
ogramming is logic-
gramming is logic-b
ramming is logic-ba
amming is logic-bas
mming is logic-base
ming is logic-based
ing is logic-based 
ng is logic-based c
g is logic-based cr
 is logic-based cre
is logic-based crea
s logic-based creat
 logic-based creati
logic-based creativ
ogic-based creativi
gic-based creativit
ic-based creativity

05 Test 5
Input
Expected output
Kitty
Kit
itt
tty


### CODE FOR THE PROBLEM ###


import sys
import math


a= input()
for i in range((len(a)//2)+1):
    for j in range(i,len(a)//2+1+i):
        print(a[j],end='')
    print()
