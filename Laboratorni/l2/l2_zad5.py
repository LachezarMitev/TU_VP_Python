a = int(input())
b = int(input())

cntr = 0
sum = 0

for i in range(a, b + 1):
    cntr += 1
    sum += i

print(f"broi: {cntr}\nsuma: {sum}")