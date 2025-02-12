num = int(input())
if num == 1:
    print("nito prosto, nito sustavno")
elif num == 2: 
    print("prosto")
else:
    cntr = 2
    while(True):
        if num % cntr == 0:
            print("sustavno")
            break
        elif cntr > num ** 0.5:
            print("prosto")
            break
        cntr += 1
