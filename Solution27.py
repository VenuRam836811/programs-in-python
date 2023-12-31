### PROBLEM ###


Hotel Tariff Calculator
Requested files: Hotel.java (Download)
Maximum number of files: 5
Type of work: Individual work
Write a  program to calculate the hotel tariff. The room rent is 20% high during peak seasons [April-June, November-December] .
Input Format:
The first line of the input contains an integer which corresponds to the number of the month. [ January is 1, Feb is 2 and so on].  
The second line of the input consists of a floating point number which corresponds to the room rent per day. 
The third line of the input consists of an integer which corresponds to the number of days stayed in the hotel.
Output Format:
Output consists of a single line which displays the hotel tariff to be payed.  
Hotel tariff should be displayed correct to 2 decimal places. 
Refer  sample output  for format details.
Sample Input 1:
3
1500
2
Sample Output 1:
Hotel Tariff: Rs.3000.00
Sample Input 2:
4
2000
2
Sample Output 2:
Hotel Tariff: Rs.4800.00


### CODE FOR THE PROBLEM ###


a=int(input())
b=float(input())
c=int(input())
if a>=4 and a<=6 or a==11 or a==12:
    d=(b+(20/100)*b)*c
    print("Hotel Tariff:Rs.",f"{d:.2f}")
else:
    e=b*c
    print("Hotel Tariff:Rs.",f"{e:.2f}")
                    
