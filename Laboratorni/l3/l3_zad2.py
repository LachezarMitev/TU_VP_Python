import random

n = int(input())
l = [random.randint(1, 21) for k in range(n)]

output = [l[0]]
for j in range(len(l) - 1):
    output += [l[j] + l[j + 1], l[j + 1]]

print(l)
print(output)