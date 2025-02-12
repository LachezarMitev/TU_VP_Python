def opr(n, x):
    for i in range(len(n)):
        if n[i] > x: n[i] = 0
    return n

nums = [int(x) for x in input().split()]
x = int(input())
print(opr(nums, x))
