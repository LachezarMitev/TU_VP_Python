inp = [float(x) for x in input().split(" ")]
l = lambda a: abs(a)
absoluteVal = [l(y) for y in inp]

print(absoluteVal)