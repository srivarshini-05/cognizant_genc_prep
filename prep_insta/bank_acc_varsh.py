'''def dep(n,t):
    t=t+n
    return t
def withi(n,t):
    t=t-n
    return t
t=100
while(True):
    s=input()
    
    if s=="d":
        n=int(input())
        t=dep(n,t)
        print(t)
    elif s=="w":
        n=int(input())
        t=withi(n,t)
        print(t)
    else:
        break'''
    
class Account:
    def  __init__(self):
        self.balance = 0
    def  depo(self, amt):
         self.balance += amt
         print(self.balance)
         
    def  withd(self, amt):
         self.balance -= amt
         print(self.balance)

a = Account()
b=Account()
a.depo(100)
a.depo(100)
a.withd(50)
b.depo(200)
b.depo(50)
b.withd(150)


         
     
    
