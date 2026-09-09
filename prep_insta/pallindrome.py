t=int(input()) #12121
n=t
a=0
while(n>0):
    r=n%10 #1
    a=a*10+r
    n=n//10
if(t==a):
    print("ys")
else:
    print("no")
    
