import sys
noTicket=int(input("Enter the no of ticket: "))

if (noTicket < 5 or noTicket > 40) :
    print("Minimum of 5 and Maximum of 40 tickets")
    sys.exit(0)

ref=input("Do you want refreshment: ")

co=input("Do you have coupon code: ")

circle=input("Enter the circle: ")
if(circle== 'k'):
    cost=75*noTicket

elif(circle== 'q'):
    cost=150*noTicket

else:
    print("Invalid Input")
    sys.exit(0)

total=cost

if(noTicket>20):
    cost= cost - ((0.1)*cost)
    total=cost

if(co== 'y'):
    total= cost - ((0.02)*cost)

if(ref== 'y'):
    total += (noTicket*50);

print("Ticket cost:{}".format(round(total,2)))
