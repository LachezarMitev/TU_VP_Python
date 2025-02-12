try:
    n = int(input())
    if n < 15 or n > 35: 
        raise ValueError("Must be between 15 and 35")
except ValueError:
    raise ValueError("Must be a number")

l1 = []
try:
    for i in range(n):
        a = int(input())
        if a < 30 or a > 300: 
            raise ValueError("Must be between 30 and 300")
        l1.append(a)
except ValueError:
        raise ValueError("Must be a number")

cntr = 0
index = -1
minN = 301
for i in l1:
    if ((i // 10) % 10) % 3 == 0:
          cntr += 1
          print(i)
    
for i in l1:
    if i % 6 == 4 and i < minN:
        index = l1.index(i)
        minN = i
    
print(cntr, index)

l2 = []
for i in l1:
    if i // 10 > 0 and i // 20 < 10 and i % 2 == 0 and i % 3 == 0:
        l2.append(i)

sum = 0
for i in range(1, len(l2), 2):
    sum += l2[i]

avg = sum / (len(l2) / 2)
print(l2, avg)

minCh = 299
maxNech = 1
minNech = 300
for i in l2:
    if i % 2 == 0 and i < minCh:
        minCh = i
    if i % 2 != 0 and i > maxNech:
        maxNech = i
    if i % 2 != 0 and i < minNech:
        minNech = i
l2.remove(minCh)
print(l2)
l2.insert(0, minNech * maxNech)
print(l2)