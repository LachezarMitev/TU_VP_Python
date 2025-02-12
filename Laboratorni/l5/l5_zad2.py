def palindrome(x):
    l = str(x)
    output = 0
    for i in range(len(l) // 2):
        if l[i] == l[len(l) - 1]: output = 1
    return output

x = int(input())
print(palindrome(x))