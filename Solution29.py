### PROBLEM ###

Budget
Requested files: Budget.java (Download)
Maximum number of files: 5
Type of work: Individual work
It’s your job to calculate the cost of replacing damaged battle droids and to check whether it is within the budget limit of Rs. 15000. The cost of the equipment and parts is given in the table below.
Blast Rifle
Rs. 350.34
Visual Sensors
Rs. 230.90
Auditory Sensors
Rs. 190.55
Arms
Rs. 125.30
Legs
Rs. 180.90
Can you write a program to do the given task?
Input:
The input consists of 5 positive integers separated by a space (A B C D E).
A: number of blast rifles needed
B: number of visual sensors needed
C: number of auditory sensors needed
D: number of arms needed
E: number of legs needed
Output:
Output consists of a single string (“yes” or “no”). Print yes if the total cost of replacing damaged battle droids is within the sanctioned budget of Rs. 15000. Print no otherwise.
Sample Input:
20 10 14 3 9
Sample Output:
yes


### CODE FOR THE PROBLEM ###


b=350.34
v=230.90
a=190.55
c=125.30
l=180.90
z=15000
a1=int(input())*b
a2=int(input())*v
a3=int(input())*a
a4=int(input())*c
a5=int(input())*l
if a1+a2+a3+a4+a5<=z:
    print("yes")
else:
    print("no")  
