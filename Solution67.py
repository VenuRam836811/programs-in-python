### PROBLEM ###

Minimum Scalar Product
Requested files: Minimum.python (Download)
Maximum number of files: 5
Type of work: Individual work
You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.
Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.
Input & Output Format:
Input consists of 1 integer and two arrays.
First input consists of an size of an array.
second inputs consists of elements of two arrays.
Output consists of a one integer.
Sample Input:
3
1 3 5
2 4 1
Sample Output:
15

### CODE FOR THE PROBLEM ###

def s(a,a1,a2):
    a1.sort()
    a2.sort()
    b=0
    for i in range(a):
        b=b+a1[i]*a2[a-i-1]
    return b

a=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
z=s(a,a1,a2)
print(z  

