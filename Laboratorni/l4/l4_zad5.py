a = input()
nums = []
lett = []
sym = []
for i in range(len(a)):
    if a[i].isdigit(): nums.append(a[i])
    elif a[i].isalpha(): lett.append(a[i])
    else: sym.append(a[i])
print(nums, lett, sym)