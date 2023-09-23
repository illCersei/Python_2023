import random as rnd
import re

def pole_fill():
    print("Игра Супер ним. 'X' - Фишки, 'O' - пуговицы\nВыиграет тот, кто заберёт последнюю фишку.")
    global pole, N, M
    pole = []
    N = 8
    M = 8
    for i in range(N):
        pole.append([" "]*M)

    for i in range(N):
        for j in range(M):
            if rnd.randint(0,5) == False:
                pole[i][j] = 'O'
            else:
                if rnd.randint(0,5) == False:
                    pole[i][j] = 'X' 

def print_pole():
    alph = [" abcdefgh"]
    for i in alph:
        print(' '.join(str(i)))
    i = 1
    for row in pole:
        print(i, end = ' ')
        for elem in row:
            print(elem, end = ' ')
        print()
        i+=1

def berem_fishki(q,n):
    counter_fish = 0
    counter_pyg = 0
    if q == 'строка': #Строка
        for i in range(N):
            if pole[n][i] == 'O':
                pole[n][i] = ' '
                counter_fish+=1
            if pole[n][i] == 'X':
                pole[n][i] = ' '
                counter_pyg +=1
    else:
        for i in range(M):
            if pole[i][n] == 'O':
                pole[i][n] = ' '
                counter_fish+=1
            if pole[i][n] == 'X':
                pole[i][n] = ' '
                counter_pyg +=1  
    if counter_fish + counter_pyg == 0:
        return -1
    print("Забрано", counter_fish, "фишек и", counter_pyg, "пуговец")
    print("Осталось", str(pole).count('O'), "фишек и", str(pole).count('X'), "пуговец")  
    return str(pole).count('O')

def valid_enter():
    while True:
        print("Напишите 'строка' или 'столбец' и её/его номер через пробел")
        input_s = input()
        try:
            s,n = input_s.split()
            if (s == 'строка' or s == 'столбец') and re.fullmatch('[1-8]', n):
                n = int(n)
                break
            else:print("Ошибка ввода")
        except ValueError:
            print("Ошибка формы ввода")
    return s,n-1 

pole_fill()
player_turn = 0
player = ""
end_game = False

while end_game == False:
    if player_turn%2 == 0:
        player = "первый"
    else:
        player = "второй"
    print("Ходит", player, "игрок")
    print_pole()
    while(True):
        q,n = valid_enter()
        d = berem_fishki(q,n)
        if d == -1:
            print("!!Строка/столбец пустые, повторите ввод")
        elif d == 0:
            print("Победил", player, "игрок")
            end_game = True
            break
        else:
            break
    print("================")
    player_turn+=1
          
     



