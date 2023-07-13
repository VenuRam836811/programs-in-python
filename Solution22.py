### PROBLEM ###


Profit or Loss
Requested files: Profit.java (Download)
Maximum number of files: 5
Type of work: Individual work
A fruitseller buys a dozen mango at Rs.X. He sells 1 mango at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.

 Input and Output Format:

Input consists of 2 floating point numbers which correspond to X and Y.

Refer sample input and output for formatting specifications. .

 Sample Input1:

60.0

4

Sample Output1:

Enter the price of a dozen mangoes

Enter the price at which 1 mango is being sold

Loss : Rs.12.00

Sample Input 2:

60.0

6

Sample Output 2:

Enter the price of a dozen mangoes

Enter the price at which 1 mango is being sold

Profit : Rs.12.00

Sample Input 3:

60.0

5

Sample Output 3:

Enter the price of a dozen mangoes

Enter the price at which 1 mango is being sold

No profit nor loss

  ### CODE FOR THE PROBLEM ###


a=float(input("Enter the price of a dozen mangoes"))
b=float(input("Enter the price at which 1 mango is being sold"))
c=b*12
if c>a:
    d=c-a
    print("Profit :RS.",end='')
    print(f"{d:.2f}")
elif c<a:
    e=a-c
    print("loss :RS.",end='')
    print(f"{e:.2f}")
else:
     print("No profit nor loss")
    
