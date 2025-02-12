#2 4 5 10 11

def zad2():
    m = int(input())
    n = int(input())
    del_tri = set(i for i in range(m, n + 1) if i % 3 == 0)
    del_chet = set(i for i in range(m, n + 1) if i % 4 == 0)
    print(del_tri ^ del_chet)

def zad4():
    txt = input()
    tp1 = tuple(txt)
    dist = int(input())
    cntr = 0
    edited_txt = []
    while(cntr < len(txt)):
        edited_txt.append(txt[cntr])
        cntr += dist
    tp2 = tuple(edited_txt)
    print(tp1, "\n", tp2)

def zad5():
    nums = [int(x) for x in input().split()]
    output = []
    sorted_n = nums
    t1 = tuple(nums)
    sorted_n.sort()
    sec_max = sorted_n[len(sorted_n) - 2]
    output += [sec_max, t1.index(sec_max)]
    print(output)

def zad10():
    import sys
    txt = input().split(" ")
    shortest = ""
    longest = ""
    min = sys.maxsize
    max = 0
    for t in txt:
        if len(t) > max:
            longest = t
            max = len(t)
        if len(t)< min:
            shortest = t
            min = len(t)
    txt.remove(shortest)
    txt.remove(longest)
    print(txt)

def zad11():
    command = input("Input: ")
    uk_bg = dict()
    while(command != "Exit"):
        if command == "Print": 
            print(uk_bg)
        elif command == "Add":
            word = input("uk add: ")
            translation = input("bg add: ")
            uk_bg[word] = translation
        elif command == "Remove":
            word = input("uk rem: ")
            del uk_bg[word]
        elif command in uk_bg:
            print(uk_bg[command])
        else:
            translation = input("bg add: ")
            uk_bg[command] = translation
        command = input("Input: ")

zad11()