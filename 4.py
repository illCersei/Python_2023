alph = ({"ноль":0, "один":1, "два":2, "три":3, "четыре":4, "пять":5, "шесть":6, "семь":7, "восемь":8, "девять":9, "десять":10, "одиннадцать":11,})
alph2 = {v:k for k, v in alph.items()}

minusxd = ""

def plus(minusxd = minusxd):
    match znak:
        case "плюс":
            res = (alph.get(s)) + alph.get(s1)
        case _:
            res = (alph.get(s)) - alph.get(s1)
    if res < 0:
        minusxd = " минус"
    print(s + ' ' + znak + ' ' + s1 + ' равно' + minusxd + ' ' + str(alph2.get(abs(res))))

while True:
    temp = input("Введите выражение ")
    try:
        s,znak,s1 = temp.split()
        if s in alph and (znak == "плюс" or znak == "минус") and s1 in alph:
            break
        else:
            print("Ошибка ввода, проверьте слова")
    except:
        print("Ошибка формы ввода")
plus()
