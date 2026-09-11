a=[4,7,2,6,5,2]
l=float('-inf')
s=float('-inf')
for i in a:
    if i>l:
        s=l
        l=i
    elif i>s  and i!=l:
        s=i
print(s)
