### PROBLEM ####


Fee Collection
Requested files: Fee.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a program to determine the fee amount to be collected from a student. The input to the program are the type of the student, tuition fee, bus fee, hostel fee.
Refer the table below for fee details.
Student Type
Student Type denoted as
Fee Details
Merit Seat Day Scholar
MSDS
Tuition fee + Bus fee
Merit Seat Hosteller
MSH
Tuition fee + Hostel fee
Management Seat Day Scholar
MGSDS
150% of Tuition fee + Bus fee
Management Seat Hosteller
MGSH
150% of Tuition fee + Hostel fee
Input and Output Format:
Input consists of a string (student type), tuition fee (float), bus fee (float) and hostel fee (float). All floating point numbers are displayed correct to 2 decimal places.
Refer sample input and output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output:
Enter the student type
MSH
Enter tuition fee
40000
Enter hostel fee
50000
The fees to be paid by the student is Rs.90000.00

### CODE FOR THE PROGRAM ###


def fee(a):
    if a=="MSDS":
        b=float(input("Enter tution fee:"))
        d=float(input("Enter bus fee:"))
        a1=b+d
        print("The fees to be paid by the student is Rs.",end='')
        print(f"{a1:.2f}")
    elif a=="MSH":
        b=float(input("Enter tution fee:"))
        c=float(input("Enter hostal fee:"))
        a2=b+c
        print("The fees to be paid by the student is Rs.",end='')
        print(f"{a2:.2f}")
    elif a=="MGSDS":
        b=float(input("Enter tution fee:"))
        d=float(input("Enter bus fee:"))
        a3=(150/100)*b+d
        print("The fees to be paid by the student is Rs.",end='')
        print(f"{a3:.2f}")
    elif a=="MGSH":
        b=float(input("Enter tution fee:"))
        c=float(input("Enter hostal fee:"))
        a4=(150/100)*b+c
        print("The fees to be paid by the student is Rs.",end='')
        print(f"{a4:.2f}")
        
    
a=input("Enter the student type:")
fee(a)
