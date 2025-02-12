import math
import random

#zad 1
def Winner(*l):
    st = []
    for i in range(len(l)):
        if len(st) == 0: 
            st.append(l[i])
        elif l[i] == st[0]: 
            st.append(l[i])
        else: 
            st.pop()
    if len(st) == 0: print("Tie")
    else: print(st[0])
#Winner("Team1", "Team2", "Team2", "Team1", "Team2")

#zad 2
def PerfNum(n):
    delitel = 2
    dl = [1]
    for i in range(int(n / 2)):
        if n % delitel == 0:
            dl.append(delitel)
        delitel += 1
    if sum(dl) == n: return True
    else: return False
# nums = [int(x) for x in input().split()]
# pNums = []
# for i in nums: 
#     if PerfNum(i): pNums.append(i)
# print(pNums)

#zad 5
def Sumi(l = [], k = []):
    sum = 0
    if len(l) < len(k):
        for i in range(len(l)):
            sum += (l[i] * k[i])
        a = 0
        for i in range(len(l), len(k)):
            sum += (l[a] * k[i])
            a += 1
    else:
        for i in range(len(k)):
            sum += (l[i] * k[i])
        a = 0
        for i in range(len(k), len(l)):
            sum += (k[a] * l[i])
            a += 1
    return sum
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8, 9, 10]
# print(Sumi(a, b))

#zad 6
def elInfo(*k):
    return [sum(k) / len(k), max(k), min(k)]
# print(elInfo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#zad 7
def txtInd(txt, *k):
    output = ""
    for i in k: 
        if i < len(txt):
            output += txt[i]
    print(output)
# txtInd("qwertyuiopa", 0, 2, 4, 6, 8, 10, 12)

#zad 8
def NOK(a, b):
    return (abs(a * b) // math.gcd(a, b))

#zad 9
def createMatr(a, b):
    matr = []
    for i in range(a):
        row = []
        for j in range(b):
            row.append(random.randint(0, 11))
        matr.append(row)
    return matr

def printMatr(m = []):
    for i in m:
        for j in i: 
            print(j, end=" ")
        print()

def sumMatr(m = []):
    cols = len(m[0])
    sums = [0] * cols
    for i in m:
        for j in range(cols):
            sums[j] += i[j]
    return sums

# m = createMatr(3, 4)
# printMatr(m)
# print(sumMatr(m))

#zad 10
def checkPrime(num):
    if num == 1:
        return "Neither"
    elif num == 2: 
        return True
    else:
        cntr = 2
        while(True):
            if num % cntr == 0:
                return False
            elif cntr > num ** 0.5:
                return True
            cntr += 1
