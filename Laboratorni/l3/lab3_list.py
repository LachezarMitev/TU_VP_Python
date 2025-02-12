import random

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l[1])
#l[1] = 11
print(l)

#coll = list(input().split(" "))
#print(coll)

b = list(i for i in range(1, 21) if i % 3 != 0)
print(b)

print(l[::-1]) # na obratno
print(l[:-1]) # bez posleden
print(l[1:]) # bez purvi
print(l[0:2]) # purvi dva
print(l[-1:]) # posleden

matr = [[1, 2, 3], [4, 5, 6], ["a", "b", "c"]]
print(matr[0] [2])

#for i in range(len(l)): print(l[i])

print(l.count(2)) # broi na daden element
print(l.index(4)) # index na el
print(min(l))
print(max(l))

l.append(22) # dobavq v kraq
l += [11, 23]
l.insert(1, 69) # dobavq po index
print(l)
l.pop(0) # maha po index
l.remove(23) # maha el sus stoinost
del l[8] # maha po index
print(l)

random.shuffle(l)
print(l)
print(random.choice(l))
l.reverse()
print(l)

l.sort()
print(l)
l.sort(reverse=True)

scoll = ["Q", "s", "d", "E", "a"]
scoll.sort(key=str.lower)
print(scoll)
scoll.sort()
print(scoll)