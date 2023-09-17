def start_game():
    global string0, string1,string2
    string0 = [" "] * 3
    string1 = [" "] * 3
    string2 = [" "] * 3

    print("Игра крестики и нолики на 3х3 поле." + '\n' +
    "Вводить нужно координаты клетки, куда вы ставите свой знак." + '\n' +
    "Первая координата - строка, вторая - столбец." + '\n' +
    "Счёт строк и столбцов от 1 до 3 включительно."'\n')
        
def print_pole():
    print("Ситуация на поле:")
    print(" _____")
    print("|" +" ".join(string0)+ "|" + "\n"+ "|" +" ".join(string1)+ "|" + "\n" + "|" + " ".join(string2)+ "|")
    print(" ‾‾‾‾‾")

def win_check(counter):
    if counter == 8:
        print("Ничья")
        return True
        
    temp = ("".join(string0) + "".join(string1) + "".join(string2))
    win = bool(0)
    if "OOO" in temp or "XXX" in temp:
        win = True
    elif string0[0] == string1[1] == string2[2] == 'X' or string0[0] == string1[1] == string2[2] == 'O' or string0[2] == string1[1] == string2[0] == 'X' or string0[2] == string1[1] == string2[0] == 'O':
        win = True
    else:
        for i in range(3):
            if string0[i] == string1[i] == string2[i] == 'X' or string0[i] == string1[i] == string2[i] == 'O':
                win = True
    if win == True:
        if counter%2 == 0:
            print("Победил первый игрок(Х)")
        else:
            print("Победил второй игрок(O)")
        return True
    
    else:
        return False
      
def player_turn(s,x,y):
    match x:
        case 0:
            if string0[y] == " ":
                string0[y] = s
                return True
        case 1:
            if string1[y] == " ":
                string1[y] = s
                return True
        case 2:
            if string2[y] == " ":
                string2[y] = s  
                return True 
        case _:
            return False
        
def player_input(s,q):
    match s:
        case 'X':
            print("Ходит первый игрок(Х)")
        case _:
            print("Ходит второй игрок(О)")
    valid_enter = bool(0)
    while valid_enter != True:
        if q == 0:
            print("Введите номер строки: ")
        else:
            print("Введите номер столбца: ")
        temp = input()
        if temp == '1' or temp == '2' or temp == '3':
            valid_enter = True
            n = int(temp)
        else:
            print("Ошибка ввода")
    
    return n-1
        
start_game()        
counter = 0
while(win_check(counter-1) == False):
    check_movement = True
    if counter%2 == 0:
        s = 'X'
    else:
        s = 'O'

    x = player_input(s,0)
    y = player_input(s,1)

    check_movement = player_turn(s,x,y)

    if check_movement == True:
        counter +=1
    else:
        print("Клетка уже занята, повторите ввод")
    print_pole()

                 


