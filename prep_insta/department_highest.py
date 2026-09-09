import sys
cse=int(input("Enter the no of students placed in CSE:"))

ece=int(input("Enter the no of students placed in ECE:"))
mech=int(input("Enter the no of students placed in MECH:"))

if(cse< 0 or ece< 0 or mech< 0):
    print("Input is Invalid")
    sys.exit()

elif(cse == ece and ece == mech ):
    print("None of the department has got the highest placement")

sys.exit()

print("Highest placement")

m=max(cse,ece,mech)

if(cse==m):
    print("CSE")

if(ece==m):
    print("ECE")

if(mech==m):
    print("MECH")
