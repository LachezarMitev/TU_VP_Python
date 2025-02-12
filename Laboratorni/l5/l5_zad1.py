def sqr(a):
    return a * a

def rect(a, b):
    return a * b

def tri(a, b):
    return (a * b) / 2

fig =  input()
if fig == "square":
    a = int(input())
    print(sqr(a))
elif fig == "rectangle":
    a = int(input())
    b = int(input())
    print(rect(a, b))
elif fig == "triangle":
    a = int(input())
    b = int(input())
    print(tri(a, b))
else: print("not a figure")

