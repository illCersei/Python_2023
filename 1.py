import random
import re

number_str = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
#print(number_str)
success = bool(0)

while success == False:
    valid_test = bool(0)
    while valid_test == False:
        print("Введите 4ёх значое число:")
        player_number_str = str(input())
        if re.fullmatch('\d\d\d\d', player_number_str):
            valid_test = True
        else:
            print("Ввод некорректен")

    korova = 0
    bik = 0
    temp = []
    for x in range(len(number_str)):
        if (player_number_str[x] in number_str) and (player_number_str[x] not in temp) :
            temp.append(player_number_str[x])
            korova+=number_str.count(player_number_str[x])
            #print("Коров найдено: ", number_str.count(player_number_str[x]))
        if number_str[x] == player_number_str[x]:
            bik+=1

    print("Быков", bik)
    print("Коров", korova)
    if bik == 4:
        success = True
        print("Победа")