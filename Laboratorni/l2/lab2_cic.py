for i in range(1, 11, 2):
    print(i, end = " ")

print()

for l in range(ord("a"), ord("z") + 1):
    print(chr(l), end = " ")

print()

n = 1
while n < 11:
    print(n)
    n += 1

x = int(input())
s = 0
while True:
    s += n % 10
    n = n // 10
    if not n:
        break
print(s)

for i in range(1, 20):
    if i == 5:
        continue
    if i == 11:
        break
    print(i)

for i in range(20, 10, -2):
    print(i, end = " ")

