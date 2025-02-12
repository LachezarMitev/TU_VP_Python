import Laboratorni.l8.figure as figure

fig =  input()
if fig == "square":
    a = int(input())
    print(figure.sqr(a))
elif fig == "rectangle":
    a = int(input())
    b = int(input())
    print(figure.rect(a, b))
elif fig == "triangle":
    a = int(input())
    b = int(input())
    print(figure.tri(a, b))
elif fig == "romboid":
    a = int(input())
    h = int(input())
    print(figure.romb(a, h))
elif fig == "trapezoid":
    a = int(input())
    b = int(input())
    h = int(input())
    print(figure.trap(a, b, h))
else: print("not a figure")