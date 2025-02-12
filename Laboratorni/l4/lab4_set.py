s = set([1, 2, 3, 1])
print(s) # izvejda bez povtoreniq

s2 = set("hello")
for i in s2:
    print(i)

s_un = s | s2 # obedinenie
print(s_un)

a = set("georgi")
b = set("ignatov")
print(a & b) # sechenie
print(a ^ b) # el koito ne suvpadat

s1 = set([2, 4 , 6])
s1.add(8)
s1.remove(2)
print(s1)
s1.remove(2) # dava KeyError: 2
s1.discard(2)
s1.pop()
s1.clear()