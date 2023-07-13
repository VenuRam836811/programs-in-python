### PROBLEM ###


Three Idiots
Requested files: Three.java (Download)
Maximum number of files: 5
Type of work: Individual work
Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line. 

Input Format: 

Input consists of 4 integers. 

The first integer corresponds to x1 . 

The second integer corresponds to y1. 

The third and fourth integers correspond to x2 and y2 respectively. 

Output Format: 

Refer Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 1 decimal place]

Sample Input:

 2

 4

 10

 15

Sample Output:

Binoy's house is located at (6.0,9.5)


### CODE FOR THE PROBLEM ###


a=int(input())
b=int(input())
c=int(input())
d=int(input())
a1=float((a+c)/2)
a2=float((b+d)/2)
print("Binoy's house is located at (",end='')
print(f"{a1:.1f}",end=',')
print(f"{a2:.1f}",end='')
print(")")
