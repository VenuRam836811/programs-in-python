### PROBLEM ###

Microwave Oven
Requested files: Microwave.java (Download)
Maximum number of files: 5
Type of work: Individual work
A microwave oven manufacturer recommends that when heating two items, add 50% to the heating time, and when heating three items double the heating time. Heating more than three items at once is not recommended. Write a program that asks the user for the number of items and the single-item heating time. The program then writes out the recommended heating time.
Input Format:
The first input is an integer which corresponds to the number of items. The second integer is a float which corresponds to the single item heating time.
Output Format:
Refer sample input and output for further formatting specifications.
Note:All text in bold corresponds to input and the rest corresponds to output
Sample Input and Output 1:
Enter the number of items
2
Enter the single item heating time
5.0
The recommended heating time is 7.50
Sample Input and Output 2:
Enter the number of items
4
Enter the single item heating time
5.0
Number of items is more


### CODE FOR THE PROBLEM ###


a=int(input("Enter the number of items\n"))
b=float(input("Enter the single item heating time\n"))
c=b+b/2
if a<=2:
    print("The recommended heating time is",f"{c:.2f}")
elif a==3:
    print("The recommended heating time is",f"{2*b:.2f}")
elif a>3:
    print("Number of items is more")
