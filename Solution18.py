### PROBLEM ###


The Discount
Requested files: Discount.java (Download)
Maximum number of files: 5
Type of work: Individual work

Mrs.Raja is a miser to the core.She saves money even on petite things. One dayshe heard a discount offer announced in a shop. she wants to purchase lot of items to save her money. The discount is given only when atleast two items are bought. Since each item has different discount prices , she finds difficult to check the amount she has saved. So she approaches you to device a automated discount calculator to make her easy while billing. 

INPUT FORMAT:

Input consists of two floating point values denoting price of item1 and item2. 

The third input denotes the discount value in percentage. 

OUTPUT FORMAT: 

The output consists of three floating values denoting total amount, discounted price and amount saved.

 Sample Input

20.50

45.40

10

Sample Output

65.90
59.31
6.59


### CODE FOR THE PROBLEM ###


w=float(input())
x=float(input())
y=float(input())
a=w+x
b=y/100
c=a*b
d=a-c
print(f"{a:.2f}")
print(f"{d:.2f}")
print(f"{c:.2f}")

