n = int(input())
output = []
for i in range(n):
    fl = input().split(" ")
    pr_num = len(fl[0])
    ppl_in = int(fl[1])
    ppl_w = int(fl[2])
    fl_output = ""
    if pr_num == ppl_in: fl_output = f"Floor {i + 1}: There are no free fitting rooms."
    else: fl_output = f"Floor {i + 1}: There are free fitting rooms."
    fl_output += f"\nFloor {i + 1}: There are {ppl_w} waiting customers. \nFloor {i + 1}: There are {pr_num - ppl_in} free fitting rooms."
    output.append(fl_output)

for str in output: print(str)