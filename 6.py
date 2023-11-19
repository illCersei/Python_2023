import random as rnd

print(f"""Игра Пятнашки. Цель игры - упорядочить размещение чисел в коробке,
разместив их по возрастанию слева направо и сверху вниз, начиная с костяшки
с номером 1 в левом верхнем углу и заканчивая пустым местом в правом нижнем углу коробки.""")

class Game:
    def __init__(self,n):
        Game.N = n
        Game.pole = []
        for i in range(Game.N):
            Game.pole.append([""]*Game.N)
        temp = [i for i in range(1,Game.N**2)]
        temp+=" "
    
        while temp:
            for i in range(Game.N):
                for j in range(Game.N):
                    Game.pole[i][j] = temp.pop(rnd.randint(0,len(temp)-1))

    def win_check(self):
        temp_list = []
        flag = True
        for i in range(Game.N):
            temp_list+= [str(i) for i in Game.pole[i]]
        
        ss = 1
        for i in temp_list[:Game.N**2-1:]:
            if i == " ":
                flag = False
                break
            elif int(i)!=ss:
                flag = False
                break
            ss+=1
        return flag
            

    def hod(self,n,dvizh):
        for i in range(Game.N):
            for j in range(Game.N):
                if Game.pole[i][j] == n:
                    x = i
                    y = j
                    break
        #print(x,y)

        match dvizh:
            case 'v':
                if x !=0:
                    if Game.pole[x-1][y] == " ":
                        Game.pole[x-1][y] = Game.pole[x][y]
                        Game.pole[x][y] = " "
                    else:print("Можно менять только с пустым полем")
                else: print("Выход за пределы поля,повторите ввод!")

            case 'n':
                if x !=Game.N-1:
                    if Game.pole[x+1][y] == " ":
                        Game.pole[x+1][y] = Game.pole[x][y]
                        Game.pole[x][y] = " "
                    else:print("Можно менять только с пустым полем")
                else: print("Выход за пределы поля,повторите ввод!")
            case 'p':
                if y !=Game.N-1:
                    if Game.pole[x][y+1] == " ":
                        Game.pole[x][y+1] = Game.pole[x][y]
                        Game.pole[x][y] = " "
                    else:print("Можно менять только с пустым полем")
                else: print("Выход за пределы поля,повторите ввод!")
            case 'l':
                if y !=0:
                    if Game.pole[x][y-1] == " ":
                        Game.pole[x][y-1] = Game.pole[x][y]
                        Game.pole[x][y] = " "
                    else:print("Можно менять только с пустым полем")
                else: print("Выход за пределы поля,повторите ввод!")


    def __str__(self):
        str_return = "*"*Game.N**2
        for i in range(Game.N):
            str_return+='\n'
            for j in range(Game.N):
                str_return+= f"{str(Game.pole[i][j]):^3} "
        str_return +='\n' + "*"*Game.N**2
        return str_return
    
while(1):
    try:
        N = int(input(f"Введите размер поля "))
        break
    except:
        print("Ошибка ввода")

pole = Game(N)
while(1):
    print(pole)
    if Game.win_check(pole):
        print("Вы победили")
        break
    cringe = ['v','n','p','l']
    while(1):
        try:
            x,y = input(f"Введите число и направление через пробел(v - вверх, n - вниз, p = вправо, l - влево) ").split()
            if 0 < int(x) < N**2 and y in cringe:
                break
            else:
                print("Ошибка ввода, числа от 1 до 15, направление написано выше")
        except:
            print("Ошибка ввода")
    Game.hod(pole,int(x),y)
    


