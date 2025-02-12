import operations as o

opr = input()
a = int(input())
b = int(input())

if opr == "+":
    print(o.Addit(a, b))
elif opr == "-":
    print(o.Subtr(a, b))
elif opr == "*":
    print(o.Mult(a, b))
elif opr == "/":
    print(o.Divis(a, b))
else:
    print("Not an operation")