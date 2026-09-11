from collections import defaultdict
s="apple"
d=defaultdict(int)
for i in s:
        d[i]+=1
    
print(d)
#mtd 2
s = "hello"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
