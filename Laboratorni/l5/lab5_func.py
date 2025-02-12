def f():
    s = "-- Inside f()"
    print(s)
print("before")
f()
print("after")

def prod(q, i, p):
    print(f"{q}, {i}, {p:.2f} bgn.")
prod(6, "banana", 3.00)
prod(q = 6, p = 3.00, i = "banana")

def mazna():
    return "foo fighters"
boba = mazna()
print(boba)

def prom(*k): # promenliv br arg w kortej
    sum = 0
    for i in k:
        sum += i
    return sum
print(prom(1, 2, 3))

def proml(l = []):
    sum = 0
    for i in l:
        sum += i
    return sum
#print(proml(int(x) for x in input().split()))

num = 10
L = lambda n: 2 * n + 1
for k in range(num):
    print(L(k), end=" ")
print()

for k in range(num):
    print((lambda x: x * x)(k + 1), end=" ")
print()

def gl():
    global vl
    vl = 10
vl = 1
print(vl)
gl()
print(vl)