def Sales(l: list):
    return len(l)

def TicketsSold(l: list):
    tNum = 0
    for s in l:
        a = s.split("->")
        tNum += int(a[1])
    return tNum

def Income(l: list):
    sum = 0
    for s in l:
        a = s.split("->")
        if int(a[0]) < 4: sum += 20 * int(a[1])
        else: sum += 15 * int(a[1])
    return sum

input = input().split(",")
print(f"Sales: {Sales(input)} \nTickets sold: {TicketsSold(input)} \nTotal income: {Income(input)}")