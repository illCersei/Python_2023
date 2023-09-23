import random as rnd
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
    print("temp a - h")
    for row in pole:
        for elem in row:
            print(elem, end = '')
        print("1 - 8")
print_pole()

def berem_fishki(q,n):
    counter_fish = 0
    counter_pyg = 0
    if q: #Строка
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
    print("Забрано", counter_fish, "фишек и", counter_pyg, "пуговец")
    print("Осталось", str(pole).count('O'), "фишек и", str(pole).count('X'), "пуговец")

print("===================")
berem_fishki(1,0)
berem_fishki(0,1)

def check_win():
    return False


while (check_win() == False):
          
     



