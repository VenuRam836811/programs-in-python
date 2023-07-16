### PROBLEM ###

Array Type
Requested files: Type.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a PYTHON program to find the type of array as whether it is even, odd or mixed. If all the elements of an array are even, then display the array type as even. If all the elements of an array are odd, then display the array type as odd. If an array has both even and odd elements, then display the array type as mixed.
Sample Input:
5
2
4
1
3
5
Sample Output:
Mixed 

### CODE FOR THE PROBLEM ###

a=int(input())
b=[]
c=d=0
for i in range(a):
    b.append(int(input()))
for i in range(a):
    if(b[i]%2==0):
        c+=1
    else:
        d+=1
if c>0 and d>0:
    print("Mixed")
elif c>0 and d==0:
    print("Even")
else:
    print("Odd")
