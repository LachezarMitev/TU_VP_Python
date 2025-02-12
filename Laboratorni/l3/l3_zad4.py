n = int(input())

l = list(i for i in range(1, n + 1))
d = {}

for i in range(len(l)):
    d[i + 1] = l[len(l) - i - 1]

print(d)