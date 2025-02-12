txt = input()
d = {}

for i in range(len(txt)):
    if txt[i] in d:
        d[txt[i]] +=1
    else:
        d[txt[i]] = 1

dk = list(d.keys())
dk.sort()
for k in dk:
    print(f"{k}: {d[k]}", end=" ")