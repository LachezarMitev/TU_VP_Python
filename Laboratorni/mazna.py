l = [0, 1, 2, 3, 4, 5]
print(l[2::2])
# for i in range(1, len(l), 2):
#     print(l[i])
l.insert(1, 11)
print(l)
del l[1]
# l.pop(1)
print(l)
t = (1, 1, 1, 1)
l2 = list(t)
l2.pop(0)
print(l2)
l3 = [int(x) for x in input().split()]
print(l3,type(l3), type(l3[0]))