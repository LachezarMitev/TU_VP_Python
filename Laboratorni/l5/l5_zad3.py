def calc(opr, a, b):
    if opr == "+":
        return a + b
    elif opr == "-":
        return a - b
    elif opr == "*":
        return a * b
    elif opr == "/":
        return a / b
    else:
        return "Not an operation"
    
o = input()
nums = [int(x) for x in input().split()]
print(calc(o, nums[0], nums[1]))