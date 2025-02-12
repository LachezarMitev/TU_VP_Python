weekdays = {
        1 : "пон",
        2 : "вт",
        3 : "ср",
        4 : "чет",
        5 : "пт",
        6 : "съб",
        7 : "нд"}
d1 = dict(fnam = "joro", lnam = "ignatov")
d2 = dict([("fnam", "aleks"), ("lnam", "olimpsa")])
print(d1)
print(d2)
print(d1["fnam"]) # po key
print("fnam" in d1) # proverqva key

d1["nam"] = "marginala"
print(d1)
del d1["nam"]
print(d1)               

for i in d1: # obhojda po keys
    print(f"{d1[i]}")