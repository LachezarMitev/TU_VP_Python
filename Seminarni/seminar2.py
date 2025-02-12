#2 8 9 10

#zad 2
def zad2():
    sum = 0
    cntr = 0
    for i in range(9, 71, 3):
        sum += i
        cntr += 1
    print(sum / cntr)

#zad 8
def zad8():
    gender = input()
    if gender == "мъж":
        acc = int(input())
        if acc >= 250000:
            print("Подходящ кандидат")
        else:
            print("Неподходящ кандидат")
    elif gender == "жена":
        waist = int(input())
        if waist >= 100:
            print("Подходящ кандидат")
        else:
            print("Неподходящ кандидат")
    else:
        print("грешка")

#zad 9
def zad9():
    weekdays = {
        1 : "пон",
        2 : "вт",
        3 : "ср",
        4 : "чет",
        5 : "пт",
        6 : "съб",
        7 : "нд"}
    curr_day = int(input())
    fut_day = int(input())
    print(weekdays[(curr_day + fut_day) % 7])

#zad 10
def zad10():
    budg = float(input())
    season = input()
    if season == "summer":
        if budg <= 100:
            print(f"Somewhere in Bulgaria\nCamp - {budg * (30 / 100):.2f}")
        elif budg > 100 and budg <= 1000:
            print(f"Somewhere in the Balkans\nCamp - {budg * (40 / 100):.2f}")
        else:
            print(f"Somewhere in Europe\nHotel - {budg * (90 / 100):.2f}")
    elif season == "winter":
        if budg <= 100:
            print(f"Somewhere in Bulgaria\nHotel - {budg * (70 / 100):.2f}")
        elif budg > 100 and budg <= 1000:
            print(f"Somewhere in the Balkans\nHotel - {budg * (80 / 100):.2f}")
        else:
            print(f"Somewhere in Europe\nHotel - {budg * (90 / 100):.2f}")
    else:
        print("err")

#zad 11
def zad11():
    j_price = 120.00
    h_price = 75.00
    s_price = 299.90

    sum = 0

    sk_num = int(input())

    for i in range(sk_num):
        j_num = int(input())
        h_num = int(input())
        s_num = int(input())

        sum += j_num * j_price + h_num * h_price + s_num * s_price

    print(f"Price {sum * 1.2:.2f} BGN")

#zad 12
def primary(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
        else: return True

def zad12():
    pr_sum = 0
    npr_sum = 0
    while True:
        num = input()
        if num == "stop": break
        elif int(num) < 0:
            print("Negative")
            continue
        elif primary(int(num)) == True:
            pr_sum += int(num)
        elif primary(int(num)) == False:
            npr_sum += int(num)
    print(f"Sum of all prime numbers: {pr_sum}\nSum of all non prime numbers: {npr_sum}")

zad12()