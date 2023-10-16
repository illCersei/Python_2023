print(f"Игроку необходимо вычеркнуть парные цифры или дающие в сумме 10."
      f"Условие - пары должны находиться рядом или через зачеркнутые цифры по горизонтали или по вертикали."
      f"После того как все возможные пары вычеркнуты, оставшиеся цифры переписываются в конец таблицы. Цель - полностью вычеркнуть все цифры.")

def init(sall):
    #print(sall)
    s = []
    for i in range(3):
        s.append([""]*9)

    count = 0
    k = 0
    for i in range(3):
        for j in range(9):
            if sall[count] == "X":
                s[i][j] = "X"
            else:
                s[i][j] = int(sall[count])
            count+=1
    return s

def print_pole(s):
    print(f"Поле:")
    print("   ", end = '')
    for i in range(1,10):
        print(f"{i} ", end = '')
    print()
    print(f"  ------------------")
    k = 1
    for i in s:
        print(f"{k}|", end = ' ')
        k+=1
        for j in i:
            print(j, end = ' ')
        print()


def hod(s,coord1, coord2):
    if (s[coord1[0]][coord1[1]] == s[coord2[0]][coord2[1]]) or (s[coord1[0]][coord1[1]] + s[coord2[0]][coord2[1]] == 10):
        s[coord1[0]][coord1[1]] = 'X'
        s[coord2[0]][coord2[1]] = 'X'
    else:
        print(f"Не выполнено условие")

def check_hods(s):
    count = 0
    for i in range(2):
        for j in range(8):
            if (s[i][j] != "X") and (s[i+1][j] == 'X') and (i == 0):
                if (s[i+2][j] == "X"):
                        pass
                elif s[i][j] == s[i+2][j] or s[i][j] + s[i+2][j] == 10:
                    count+=1
            if (s[i][j] != "X") and (s[i+1][j] != 'X'):
                if s[i][j] == s[i+1][j] or s[i][j] + s[i+1][j] == 10:
                    count+=1

    for k in range(3):
        temp = "".join(str(i) for i in s[k] if i!='X')
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1] or (int(temp[i]) + int(temp[i+1]) == 10):
                count+=1
    #print(count) #ходов осталось
    return count
            
def input_coords(s):
    while(1):
        coord1 = []
        coord2 = []
        while(1):
            try:
                x,y = input(f"Введите координаты первого эелемента через пробел ").split()
                if 1<=int(x)<=3 and 1<=int(y)<=9:
                    coord1.append(int(x) - 1)
                    coord1.append(int(y) - 1)
                    break
                else:
                    print(f"Ошибка ввода первого элемента, повторите")
            except:
                print(f"Ошибка ввода формы первого элемента")
        
        while(1):
            try:
                x,y = input(f"Введите координаты второго эелемента через пробел ").split()
                if (1<=int(x)<=3 and 1<=int(y)<=9):
                    coord2.append(int(x) - 1)
                    coord2.append(int(y) - 1)
                    break
                else:
                    print(f"Ошибка ввода второго элемента, повторите")
            except:
                print(f"Ошибка ввода формы второго элемента")

        valid = True
        if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
            if s[coord1[0]][coord1[1]] == 'X' or s[coord2[0]][coord2[1]] == 'X':
                valid = False
            else:
                if (coord1[1] == coord2[1]):
                    if (abs(coord1[0] - coord2[0]) == 2  and s[1][coord1[1]] == 'X') or (abs(coord1[0] - coord2[0]) == 1):
                        pass
                    else:
                        valid = False

                if valid:
                    if (coord1[0] == coord2[0]):
                            if coord2[1] < coord1[1]:
                                x = coord2[1]
                                y = coord1[1]
                            else:
                                x = coord1[1]
                                y = coord2[1]
                            temp = "".join(str(i) for i in s[coord1[0]])
                            temp = temp[x+1: y]
                            if len(temp) == temp.count("X"):
                                pass
                            else:
                                valid = False
        else:
            valid = False

        if valid:
            break
        else:
            print(f"Ошибка вовода координат")
    return coord1,coord2

def win_check(s):
    temp = ""
    for i in range(3):
        temp = temp + "".join(str(i) for i in s[i])
    if temp.count('X') == 27:
        return 1
    else:
        return 0

def pererisovka(s):
    temp = ""
    for i in range(3):
        temp = temp + "".join(str(i) for i in s[i])
    temp = temp2 = list(temp)
    i = 0
    for j in temp:
        if j == "X":
            temp2.pop(i)
            temp2.insert(0, "X")
        i+=1
    #print(("".join((str(i) for i in temp2))))
    print(f"Ходы закончились, оставшиеся цифры переписываются в конец таблицы")
    return ("".join((str(i) for i in temp2)))

#sall = "123456789111213141516171819" 
s = init("123456789111213141516171819")
print_pole(s)

while(1):
    while(check_hods(s)):
        coord1,coord2 = input_coords(s)
        hod(s,coord1, coord2)
        print_pole(s)
    s = init(pererisovka(s))
    print_pole(s)

    if win_check(s) == 1:
        print(f"Вы выиграли")
        break

    if check_hods(s) == 0:
        print(f"Вы проиграли")
        break

